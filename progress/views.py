from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from progress.models import Progress
from progress.serializers import ProgressSerializer


class ProgressViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], url_path="progress")
    def my_progress(self):
        progresses = Progress.objects.filter(student=self.request.user)
        serializer = ProgressSerializer(progresses, many=True)
        return Response(serializer.data)
