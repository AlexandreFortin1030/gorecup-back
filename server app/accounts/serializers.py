from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

from.models import User


class SignupSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8, write_only=True)
    class Meta(object):
        model = User
        fields = ["username", "password"]

    def validate(self, attrs):
        username_exist=User.objects.filter(username=attrs['username']).exists()

        if username_exist:
            raise ValidationError("Username has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)
        return user
