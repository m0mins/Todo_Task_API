from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

from .models import TodoItem, UserRole
from .serializers import TodoItemSerializer,UserRoleSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .permissions import IsAdminOrStaff

#Registration
class UserRegistrationAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        role = data.get('role', 'other') 

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            user_role = UserRole(user=user, role=role)
            print(user_role)
            user_role.save()

            refresh = RefreshToken.for_user(user_role)
            return Response({ 'message': 'User registered successfully'})
            #return Response({ 
            #    'refresh': str(refresh),
            #    'access': str(refresh.access_token), 
            #    'message': 'User registered successfully'})
        except IntegrityError:
            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

#Login
class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'access': str(refresh.access_token), 
                })
           
        
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)