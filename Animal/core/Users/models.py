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
        related_name='charging_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                    'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='charging_user_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



