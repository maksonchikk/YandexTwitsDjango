from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly

class IsAutorOrReadOnly(IsAuthenticatedOrReadOnly):


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            obj.author == request.user
        )