from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import NotFound
from rest_framework import generics, filters, status
from apps.users import constants
from apps.cards.serializers import *
from apps.cards.exceptions import ProductNotFoundError, AlreadyInFavoritesError 
from apps.cards.services import (
    get_favorite_product,
    is_event_in_favorites,
    add_product_to_favorites,
    remove_product_from_favorites,
)
# Create your views here.
class FavoriteListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        product = (user)

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
