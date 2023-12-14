from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.utils.decorators import method_decorator

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})

            else:
                user = User.objects.create_user(email=email, password=password, name=name)
                user.save()
                return Response({'success': 'User created successfully'})

        else:
            return Response({'error': 'Passwords do not match'})

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = MyTokenObtainPairSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import UserAccount
from .serializers import RealtorSerializer

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserAccount.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None


class RealtorView(RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = RealtorSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserAccount.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None

