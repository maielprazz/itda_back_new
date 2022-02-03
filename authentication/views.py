from rest_framework import generics,status
from .serializers import RegisterSerializers, LoginSerializer
from rest_framework.response import Response
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .renderers import UserRenderer
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

# Create your views here.
class RegisterView(generics.GenericAPIView):

  serializer_class=RegisterSerializers
  renderer_classes = (UserRenderer,)

  def post(self,request):
    user=request.data
    serializer=self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user_data=serializer.data

    user = User.objects.get(email=user_data['email'])

    return Response(user_data, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
  serializer_class = LoginSerializer
  def post(self,request):
    serializer = self.serializer_class(data = request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
