from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User
from core import settings


User = settings.AUTH_USER_MODEL

# Create your models here.
class CustomUsers(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)  
    contact_number = models.CharField(max_length=10, unique=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=255, default=1)
    is_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customusers_set',  # Change the related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customusers_set',  # Change the related name
        blank=True,
        help_text='Specific permissions for this user.'
    )
    def __str__(self):
        return self.username



