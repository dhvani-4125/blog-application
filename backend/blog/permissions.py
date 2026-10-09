from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class IsOwnerOrStaffOrReadOnly(BasePermission):
    """Anyone may read; only the author or staff may change or delete."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        owner = getattr(obj, 'author', None) or getattr(obj, 'user', None)
        return bool(request.user and request.user.is_authenticated
                    and (request.user.is_staff or owner == request.user))
