from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'pet_image']

class PetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PetCategory
        fields = '__all__'