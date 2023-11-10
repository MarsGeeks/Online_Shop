from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import NotFound
from rest_framework import generics, filters, status
from apps.users import constants
from rest_framework.viewsets import ModelViewSet
from apps.cards.serializers import *
from apps.cards.exceptions import ProductNotFoundError, AlreadyInFavoritesError
from apps.cards.services import (
    get_favorite_product,
    is_event_in_favorites,
    add_product_to_favorites,
    remove_product_from_favorites,
    get_product,
    get_events_by_subcategory
)
# Create your views here.
class ProductListAPIView(APIView):
    serializer_class = ProductSerializer
    lookup_field = 'id'
    def get(self, request):
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)  # Сериализуем продукты
        return Response(serializer.data)
    def get_queryset(self):
        return get_product()

class ProductDetailAPIView(ModelViewSet):
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    queryset = get_product()

class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubCategoryProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        subcategory_id = self.kwargs['id']
        queryset = get_events_by_subcategory(subcategory_id)
        return queryset

class FavoriteListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        product = Product.objects.filter(userfavoriteproduct__user=user)
        paginator = PageNumberPagination()
        paginator.page_size = 10

        page = paginator.paginate_queryset(product, request)

        serialized_product = ProductSerializer(page, many=True)
        data = serialized_product.data

        for product_data in data:
            product_id = product_data.get('id')
            product_data['selected'] = is_event_in_favorites(user, product_id)
        return paginator.get_paginated_response(data)

class AddToFavoritesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id, format=None):
        user = request.user
        try:
            product = add_product_to_favorites(user, product_id)
            return Response({'message': 'Событие добавлено в избранное'}, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except AlreadyInFavoritesError:
            return Response({'message': 'Событие уже в избранном'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Невозможно добавить событие в избранное'}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromFavoritesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id, format=None):
        user = request.user
        remove_product_from_favorites(user, product_id)
        return Response({'message': 'Событие удалено из избранного'}, status=status.HTTP_200_OK)

class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        serialized_cart_items = CartItemSerializer(cart_items, many=True)
        return Response(serialized_cart_items.data, status=status.HTTP_200_OK)

class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user = request.user
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        return Response({'message': 'Товар добавлен в корзину'}, status=status.HTTP_200_OK)

class RemoveFromCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, cart_item_id):
        try:
            cart_item = CartItem.objects.get(pk=cart_item_id)
            cart_item.delete()
            return Response({'message': 'Товар удален из корзины'}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'message': 'Такой товар не найден в корзине'}, status=status.HTTP_404_NOT_FOUND)