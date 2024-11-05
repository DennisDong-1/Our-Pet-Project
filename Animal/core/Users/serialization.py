from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password','contact_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            contact_number = validated_data['contact_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user