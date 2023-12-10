from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)  # Corrected line

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = self.user.email  # Use email or any other user attribute you want
        data['email'] = self.user.email

        return data
