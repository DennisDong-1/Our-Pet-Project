from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class PetSerializer(serializers.Serializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'pet_image']

class PetCategorySerializer(serializers.Serializer):
    class Meta:
        model = PetCategory
        fields = '__all__'