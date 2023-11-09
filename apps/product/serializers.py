from rest_framework import serializers
from apps.product.models import *
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['image', 'get_full_name']

class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ['user', 'text', 'datetime']