from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from progress.models import Assignment
from progress.serializers import AssignmentSerializer
from rest_framework.exceptions import PermissionDenied


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="mark-completed")
    def mark_completed(self, request,pk=None, tuition_pk=None):
        assignment = self.get_object()

        if assignment.tuition.tutor != request.user:
            PermissionDenied("You dont create it")


        assignment.is_completed = True
        assignment.save()
        return Response({"status": "Assignment marked as completed"})
