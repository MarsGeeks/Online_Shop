from rest_framework import serializers
from apps.cards.models import *

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
    subcategory = SubCategorySerializer(many=True,read_only=True, label='категория')
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'rating', 'subcategory']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity')