from rest_framework import permissions


class HasAInUsername(permissions.BasePermission):
    message = {"success": False, "message": "Kullanıcı adınınzda A harfi yok"}

    def has_permission(self, request, view):
        if request.user.username.__contains__("a"):
            return True
        return False
