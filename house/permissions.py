from rest_framework import permissions


class IsHouseManagerOrNone(permissions.BasePermission):
    """
    Custom permissions for House Managers to only allow specific privileges to edit specific house attributes.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or not request.user.is_anonymous

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.profile == obj.manager
