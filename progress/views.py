from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from progress.models import Progress, Assignment
from progress.serializers import ProgressSerializer, AssignmentSerializer


class ProgressViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProgressSerializer

    # @action(detail=False, methods=["get"], url_path="progress")
    def my_progress(self):
        progresses = Progress.objects.filter(student=self.request.user)
        serializer = ProgressSerializer(progresses, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Progress.objects.filter(student=self.request.user)


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    @action(detail=True, methods=["post"], url_path="mark-completed")
    def mark_completed(self, request, pk=None):
        assignment = self.get_object()
        assignment.is_completed = True
        assignment.save()
        return Response({"status": "Assignment marked as completed"})
