from django.shortcuts import render
from rest_framework import viewsets, generics
from .serialization import *
from .models import *
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()



# For Login/Logout

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email = email, password = password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "role": user.role,
                    "email": email,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "success": "Login Successful",
                },
            )
        else:
            return Response({"error": "Wrong Credentials"}, status = HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({"error": str(e)})
        
class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    