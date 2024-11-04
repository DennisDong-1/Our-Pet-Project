from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUsers(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)  
    contact_number = models.CharField(max_length=10, unique=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=255, default='Adopters')
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
    
# class AdopterProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='adopter_profile')
#     adoption_history = models.TextField(blank=True, null=True)
#     pet_preference = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.email} - Adopter Profile"
    
# class RehomerProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='rehomer_profile')
#     # organization_name = models.CharField(max_length=255, blank=True, null=True)
#     rehomer_experience = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.email} - Rehomer Profile"


