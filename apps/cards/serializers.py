from rest_framework import serializers
from apps.cards.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = '__all__'
        