from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer
from .serializers import RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user = CustomUser.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        token = Token.objects.create(user=user)
        return Response({'token': token.key})

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)
