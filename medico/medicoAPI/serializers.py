from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Medicine


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'price', 'quantity', 'expiry', 'description']
