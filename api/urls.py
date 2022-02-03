from django.urls import path
from . import views

urlpatterns = [
    path('storemaster/', views.StoreMasterAPIView.as_view(), name='storemaster'),
    path('listserver/', views.ListServerAPIView.as_view(), name='listserver'),
    path('test/', views.ListMenuAcessAPIView.as_view(), name='test'),
]
