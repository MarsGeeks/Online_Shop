from rest_framework import serializers
from apps.cards.models import *
from apps.product import serializers as product_serializer
from apps.product.models import Review
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields ='__all__'
class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True,read_only=True, label='категория')
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id','title','description','price', 'rating', 'subcategory']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = product_serializer.ImageProductSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True, label='категория')
    reviews = product_serializer.ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'images', 'title', 'description', 'price', 'rating', 'subcategory', 'reviews']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        reviews_data = product_serializer.ReviewSerializer(Review.objects.filter(product=instance), many=True).data
        representation['reviews'] = reviews_data
        return representation

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity')