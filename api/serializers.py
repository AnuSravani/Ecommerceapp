from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Products,Categories




class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=User
        fields=[
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            
        ]

    
class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    is_available=serializers.BooleanField(read_only=True)
    class Meta:
        model=Categories
        fields=[
            "id",
            "title",
            "is_available"
        ]
class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    customer=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"
        