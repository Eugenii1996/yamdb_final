from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrModeratorOrOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            request.method in SAFE_METHODS
            or user.is_moderator()
            or user.is_admin()
            or obj.author == request.user
        )


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.user.is_authenticated:
            return (
                user.is_admin()
            )
        return request.method in SAFE_METHODS


class IsAdmin(BasePermission):
    """Права только у админа"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()
