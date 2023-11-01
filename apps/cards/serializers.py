from rest_framework import serializers
from apps.cards.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','description','price', 'rating']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_image', 'price', 'title', 'description']

