from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view):
        return request.user == view.get_object().owner
