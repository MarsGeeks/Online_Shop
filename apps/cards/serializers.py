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
        fields = ['title','description','price', 'rating', 'subcategory']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_image', 'price', 'title', 'description']

