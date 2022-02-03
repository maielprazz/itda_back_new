from rest_framework import serializers

# from itda_back.authentication.models import User
from .models import StoreMasterModel
from .models import *
from useraccessmenu.models import UserAccessMenu

class StoreMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreMasterModel
        fields = '__all__'  
  
class ServerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerListModel
        fields = '__all__'  

class UserAccessMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccessMenu
        fields = '__all__'          
