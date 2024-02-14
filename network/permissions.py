from rest_framework import permissions


class DebtUpdatePermission(permissions.BasePermission):
    """
    User permission to prevent debt from being updated.
    """
    message = 'You do not have permission to updated debt'

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH'] and 'debt' in request.data:
            return False
        return True
