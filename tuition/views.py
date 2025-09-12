from applications.serializers import ApplicationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from tuition.serializers import TuitionSerializer
from tuition.models import Tuition
from applications.models import Application
from progress.models import Assignment
from progress.serializers import AssignmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from reviews.serializers import ReviewSerializer


class TuitionViewSet(ModelViewSet):
    http_method_names = ["get", "patch", "delete", "post"]
    serializer_class = TuitionSerializer
    queryset = Tuition.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "class_level": ["exact"],
        "subject": ["icontains", "iexact"],
        "tutor": ["exact"],
    }

    def perform_create(self, serializer):
        if not self.request.user.is_tutor:
            raise PermissionDenied("Only tutors can create tuitions")
        serializer.save(tutor=self.request.user)

    def perform_update(self, serializer):
        tuition = self.get_object()

        if not self.request.user.is_tutor:
            raise PermissionDenied("Only tutors can edit tuitions")

        if tuition.tutor != self.request.user:
            raise PermissionDenied("Only author can change tuitions descriptions")

        serializer.save()

    def perform_destroy(self, object):
        tuition = self.get_object()
        if not self.request.user.is_tutor:
            raise PermissionDenied("Only tutors can delete tuitions")

        if tuition.tutor != self.request.user:
            raise PermissionDenied("Only author can delete tuitions")

        object.delete()

    @action(detail=True, methods=["post"])
    def apply(self, request, pk=None):
        if not request.user.is_student:
            raise PermissionDenied("Only students can apply")

        tuition = get_object_or_404(Tuition, id=pk)

        if Application.objects.filter(user=request.user, tuition=tuition).exists():
            return Response(
                {"detail": "Already applied"}, status=status.HTTP_400_BAD_REQUEST
            )

        Application.objects.create(user=request.user, tuition=tuition)
        return Response(
            {"detail": "Applied successfully"}, status=status.HTTP_201_CREATED
        )

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
        url_path="select/(?P<applicant_id>[^/.]+)",
    )
    def select(self, request,pk=None,applicant_id=None):
        tuition = self.get_object()

        if not request.user.is_tutor:
            raise PermissionDenied("Only tutor can access this endpoint")

        if request.user != tuition.tutor:
            raise PermissionDenied(
                "Only the tutor who created tuition can select applicants"
            )

        application = Application.objects.get(tuition=tuition, user_id=applicant_id)
        if application:
            application.is_selected = True
            application.save()
            return Response(ApplicationSerializer(applications, many=True).data)

        return Response(
            {"error": "Applicant not found"}, status=status.HTTP_404_NOT_FOUND
        )
    
    def add_assignment(self, request, pk=None):
        tuition = self.get_object()
        student_id = request.data.get("student_id")

        assignment = Assignment.objects.create(
            tuition=tuition,
            student_id=student_id,
            title=request.data["title"],
            description=request.data.get("description", ""),
        )
        return Response(AssignmentSerializer(assignment).data)
