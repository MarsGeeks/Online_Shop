from apps.users.models import User
from rest_framework import serializers
from apps.users import constants, models
from rest_framework.exceptions import ValidationError


class PasswordResetNewPasswordSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    password = serializers.CharField(
        style={"input_type": "password"}, min_length=4
    )


class PasswordResetCodeSerializer(serializers.Serializer):
    code = serializers.CharField()


class PasswordResetSearchUserSerializer(serializers.Serializer):
    email = serializers.CharField()

    def validate_email(self, email):
        try:
            models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            return ValidationError(
                f"Пользователь с указанным адресом электронной почты не найден."
            )
        return email


class UserRegistrationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("firstname", "lastname", "email", "birthday", "gender", "password")


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="min length 3", min_length=3
    )


class LogoutSerailiser(serializers.Serializer):
    refresh = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id product_image firstname lastname email'.split()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['product_image', 'firstname', 'lastname', 'gender', 'birthday']

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.image = validated_data.get('product_image', instance.image)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
