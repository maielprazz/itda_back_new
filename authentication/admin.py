from django.contrib import admin
from authentication.models import User
from useraccessmenu.models import MainMenu,UserAccessMenu
from rest_framework_simplejwt import token_blacklist

class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

   def has_delete_permission(self, * args, ** kwargs):
    return True # or whatever logic you want

# Register your models here.
admin.site.register(User)
admin.site.register(MainMenu)
admin.site.register(UserAccessMenu)
admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)