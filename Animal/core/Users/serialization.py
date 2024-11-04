from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = '__all__'