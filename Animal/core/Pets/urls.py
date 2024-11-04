from django.urls import path
from .views import *

urlpatterns = [
    path('petsList', PetListView.as_view(), name='pets'),
    path('petsRetrieve',PetRetrieveView.as_view(), name='pets'),
    path('petsUpdate',PetUpdateView.as_view(), name='pets'),
    path('petsDelete',PetDeleteView.as_view(), name='pets'),

    path('petsCategory',PetCategoryListView.as_view(), name='pets'),
    path('petsCategoryRetrieve',PetCategoryRetrieveView.as_view(), name='pets'),
    path('petsCategoryUpdate',PetCategoryUpdateView.as_view(), name='pets'),
    path('petsCategoryDelete',PetCategoryDeleteView.as_view(), name='pets'),
]