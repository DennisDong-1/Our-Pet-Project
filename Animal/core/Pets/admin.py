from django.contrib import admin
from .models import *

# Register your models here.

class PetDetails(admin.ModelAdmin):
    list_display = ['id', 'pet_image', 'name']
    search_fields = ['name']

admin.site.register(Pet, PetDetails)
admin.site.register(PetCategory)