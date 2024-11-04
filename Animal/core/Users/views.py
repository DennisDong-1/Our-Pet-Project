from django.shortcuts import render
from rest_framework import viewsets, generics
from .serialization import *
from .models import *

# Create your views here.

class CustomUsersView(generics.ListAPIView):
    queryset = CustomUsers.objects.all()
    serializer_class = CustomUsersSerializer
