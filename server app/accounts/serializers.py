from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

from.models import User


class SignupSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8, write_only=True)
    class Meta(object):
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email_exist=User.objects.filter(email=attrs['email']).exists()

        if email_exist:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)
        return user

class CurrentUserPetSerializer(serializers.ModelSerializer):

    pets = serializers.HyperlinkedRelatedField(
        many=True, view_name="pet-detail", queryset=User.objects.all()
        )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'pets']

class CurrentUserPostSerializer(serializers.ModelSerializer):

    pets = serializers.HyperlinkedRelatedField(
        many=True, view_name="post-detail", queryset=User.objects.all()
        )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'pets', 'post']
