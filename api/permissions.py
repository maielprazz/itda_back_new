from rest_framework import permissions

class SVRPermissions(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")
    
    def has_permission(self, request, view):
        if "_SVR" in request.user.get_accesscode() :
          return True
        if request.user.is_superuser:
          return True 
        if request.user.is_staff:
          return True 
        return False
