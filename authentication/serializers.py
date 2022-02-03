from rest_framework import serializers
import json
from authentication.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterSerializers(serializers.ModelSerializer):
  password = serializers.CharField(max_length=68, min_length=6, write_only=True)

  class Meta:
    model=User
    fields=['email','username','password']


  def create(self, validated_data):
      return User.objects.create_user(**validated_data)


''' LOGIN API '''
class LoginSerializer(serializers.ModelSerializer, TokenObtainPairSerializer):
  username = serializers.CharField(max_length=150, min_length=3)
  password = serializers.CharField(max_length=68, min_length=2, write_only=True)
  refresh = serializers.CharField(max_length=255, min_length=3, read_only=True)
  access = serializers.CharField(max_length=255, min_length=3, read_only=True)
  drawmenu = serializers.ListField(max_length=255, min_length=3, read_only=True)
 

  class Meta:
    model = User
    fields = ['username','password','refresh', 'access', 'drawmenu']

  @classmethod
  def get_tokens(cls, user, **kwargs):
    token = super().get_token(user)

    accesscode = kwargs.get('accesscode')
    # Add custom claims
    token['username'] = user.username
    token['display_name'] = user.display_name
    token['email'] = user.email
    token['accesscode'] = accesscode
  
    return {"refresh": str(token), "access": str(token.access_token)} 
  

  def validate(self,attrs):
    
    username = attrs.get('username', '')
    password = attrs.get('password','')
    user = auth.authenticate(username = username, password = password)
    # import pdb
    # pdb.set_trace()
    if not user:
      raise AuthenticationFailed('Invalid credentials, Try again')

  
    mytokens = self.get_tokens(user, accesscode = user.get_accesscode)
    data = {   "username": user.username,
      "drawmenu" : user.get_drawer
      }

    data['refresh'] = mytokens['refresh']
    data['access'] = mytokens['access']
    
    return data
  



    