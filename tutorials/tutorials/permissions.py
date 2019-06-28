from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS :
            return True
        
        return request.user.is_staff


