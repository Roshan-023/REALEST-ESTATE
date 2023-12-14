from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   @classmethod
   def get_token(cls, user):
    token = super().get_token(user)
    token['username'] = user.name
    return token


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ['groups', 'user_permissions']
