from rest_framework.permissions import BasePermission

class IsList(BasePermission):

    def has_permission(self, request, view):

        # IF THIS IS A LIST VIEW, CHECK ACCESS LEVEL
        if (view.action == 'list' ):
            return False
        else :
            return True    