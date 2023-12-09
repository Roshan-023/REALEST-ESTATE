from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   def validate(self, attr):
    data = super().validate(attr)
    token = self.get_token(self.user)
    data['refresh'] = str(refresh)
    data['access'] = str(refresh.access_token)
    data['user'] = str(self.user)
    data['email'] = self.user.email

    return data

