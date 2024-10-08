from rest_framework import permissions


class IsAllowedToEditTaskListElseNone(permissions.BasePermission):
    """
    Custom permissions for TaskListViewSet to only allow the creator editing permissions.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or not request.user.is_anonymous

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by


class IsAllowedToEditTaskElseNone(permissions.BasePermission):
    """
    Custom permissions for TaskViewSet to only allow members of a house access to its tasks.
    """

    def has_permission(self, request, view):
        # if not request.user.is_anonymous:
        #     return request.user.profile.house is not None
        return request.user.profile.house is not None if not request.user.is_anonymous else False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task_list.house


class IsAllowedToEditAttachmentElseNone(permissions.BasePermission):
    """
    Custom permissions for Attachment to only allow members of a house access to its tasks.
    """

    def has_permission(self, request, view):
        return request.user.profile.house is not None if not request.user.is_anonymous else False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task.task_list.house
