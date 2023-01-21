from rest_framework import permissions


class IsEmployee(permissions.BasePermission):

    def has_permission(self, user_obj, perm, obj=None):
        return user_obj.user.is_employee
