from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class CustomPerm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        raise PermissionDenied({"message":"You don't have permission to access",
                                "object_id": obj.id})