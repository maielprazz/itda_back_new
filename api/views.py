from rest_framework.generics import ListAPIView
from .permissions import SVRPermissions
from .models import *
from .serializers import *
from django.db import connections
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from useraccessmenu.models import UserAccessMenu

class StoreMasterAPIView(ListAPIView):
  serializer_class=StoreMasterSerializer
  # queryset = StoreMasterModel.objects.using('sql2').raw("SELECT Sitecode , Lc_regrouping,  Area,  Sbu,  Status,  Sitecode_old,  Startdate,  Enddate,  Site_category, Site_subcategory FROM SITE_REFFERENCE")
  queryset = StoreMasterModel.objects.using('sql2').raw("EXEC SP_GENERATE_DATA '3','','',''")
  # permission_classes = (permissions.IsAuthenticated,)


class ListServerAPIView(ListAPIView):
  serializer_class=ServerListSerializer
  queryset = ServerListModel.objects.using('sql2').raw("EXEC SP_GENERATE_DATA '4','','',''")

class ListMenuAcessAPIView(ListAPIView):
  authentication_classes = [BasicAuthentication]
  permission_classes = [SVRPermissions,IsAuthenticated]
  serializer_class=UserAccessMenuSerializer
  queryset = UserAccessMenu.objects.all()  
