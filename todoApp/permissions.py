from rest_framework import permissions
from todoApp.models import UserRole

class IsAdminOrStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            user_role = UserRole.objects.get(user=request.user)
        except UserRole.DoesNotExist:
            return False

        #if request.user.is_superuser or (user_role.role == 'admin'):
        if user_role.role == 'admin':
           return True
        elif user_role.role == 'staff':
           return request.method in ['POST', 'PUT', 'PATCH'] or request.method in permissions.SAFE_METHODS 
         #Others can only read
        return request.method in permissions.SAFE_METHODS