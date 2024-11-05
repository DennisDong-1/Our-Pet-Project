from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Permission, Group
from core import settings


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(unique=False)
    breed = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    description = models.TextField()  
    posted_at = models.DateTimeField(auto_now_add=True)
    pet_image = models.ImageField(upload_to="category/",null=True, blank=True )
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.breed} and {self.category}"

class PetCategory(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name