from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

admin.site.site_header = 'ITDA Web Portal Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('auth/',include('authentication.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]
