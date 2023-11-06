from rest_framework import serializers
from apps.product.models import *
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['product_image', 'get_full_name']

class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['user', 'text']