from reviews.serializers import ReviewSerializer
from reviews.models import Review
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from applications.models import Application
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from reviews.permissions import IsReviewOwnerOrReadOnly

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,IsReviewOwnerOrReadOnly]
    
    def get_queryset(self):
        tuition_id = self.kwargs.get("tuition_pk")
        return Review.objects.filter(tuition_id=tuition_id)

    def perform_create(self, serializer):
        tuition_id = self.kwargs.get("tuition_pk")
        user = self.request.user

        if not user.is_student:
            raise PermissionDenied("Only students can leave reviews.")

        if not Application.objects.filter(tuition_id=tuition_id, user=user, is_selected=True).exists():
            raise PermissionDenied("This tutor dont teach you")
        
        serializer.save(user=user, tuition_id=tuition_id)