from rest_framework import permissions
from todoApp.models import UserRole

class IsAdminOrStaff(permissions.BasePermission):
    """
    Custom permission to allow admins to do everything,
    staff to create and update, and others only to read.
    """

    def has_permission(self, request, view):
        try:
            # Attempt to get the user's UserRole instance
            user_role = UserRole.objects.get(user=request.user)
        except UserRole.DoesNotExist:
            # If the UserRole doesn't exist, return False
            return False

        # Allow admins to do everything
        #if request.user.is_superuser or (user_role.role == 'admin'):
        if user_role.role == 'admin':
           return True
        # Allow staff to create and update
        elif user_role.role == 'staff':
           return request.method in ['POST', 'PUT', 'PATCH'] or request.method in permissions.SAFE_METHODS 
         #Others can only read
        return request.method in permissions.SAFE_METHODS