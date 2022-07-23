from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner != request.user:
            return False
        return super().has_object_permission(request, view, obj)
