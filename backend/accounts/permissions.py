from rest_framework import permissions

class HasAccess(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.has_perm("accounts.change_user"):
            return True
        
        username = view.kwargs.get("username", None)
        if username is not None:
            if request.user.username == username:
                return True

        return False