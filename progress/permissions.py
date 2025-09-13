from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTutor(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.is_tutor 
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.tuition.tutor == request.user
