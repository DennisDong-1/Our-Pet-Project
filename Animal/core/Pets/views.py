from django.shortcuts import render
from rest_framework import viewsets, generics
from .serialization import *
from .models import *

# Create your views here.

#For Pets
class PetListView(generics.ListAPIView):
    model = Pet
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        return Pet.objects.all()

class PetRetrieveView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetUpdateView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetDeleteView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

#For PetCategorys

class PetCategoryListView(generics.ListCreateAPIView):
    queryset = PetCategory.objects.all()
    serializer_class = PetCategorySerializer

class PetCategoryRetrieveView(generics.CreateAPIView):
    queryset = PetCategory.objects.all()
    serializer_class = PetCategorySerializer

class PetCategoryUpdateView(generics.UpdateAPIView):
    queryset = PetCategory.objects.all()
    serializer_class = PetCategorySerializer

class PetCategoryDeleteView(generics.DestroyAPIView):
    queryset = PetCategory.objects.all()
    serializer_class = PetCategorySerializer