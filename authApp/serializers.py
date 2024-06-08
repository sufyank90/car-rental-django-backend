from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import CarDetail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# class CarDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarDetail
#         fields = '__all__'
