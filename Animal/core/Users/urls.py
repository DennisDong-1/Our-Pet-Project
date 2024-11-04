from django.urls import path, include
from .views import *

urlpatterns = [
    path('customusers', CustomUsersView.as_view(), name='customusers'),
]