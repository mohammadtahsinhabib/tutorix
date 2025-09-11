from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from tuition.serializers import *
from .models import Tuition, Application
from django_filters.rest_framework import DjangoFilterBackend


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

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated])
    def applicants(self, request, pk=None):
        tuition = self.get_object()

        if not request.user.is_student:
            raise PermissionDenied("Only student can access this endpoint")

        if request.user != tuition.tutor:
            raise PermissionDenied("Permission Denied")

        applications = Application.objects.filter(tuition=tuition)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
        url_path="select/(?P<applicant_id>[^/.]+)",
    )
    def select(self, request):
        tuition = self.get_object()

        if not request.user.tutor:
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

    @action(detail=True, methods=["post", "get"], permission_classes=[IsAuthenticated])
    def reviews(self, request, pk=None):
        tuition = self.get_object()

        if request.method == "GET":
            reviews = Review.objects.filter(tuition=tuition)
            return Response(ReviewSerializer(reviews, many=True).data)

        if request.method == "POST":
            if not self.request.user.is_student:
                raise PermissionDenied("Only students can leave reviews.")

            if not Application.objects.filter(
                tuition=tuition, user=request.user, is_selected=True
            ).exists():
                raise PermissionDenied("This tutor doesnt tutioned you")

            serializer = ReviewSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user, tuition=tuition)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], url_path="status")
    def mark_topic_completed(self, request, pk=None):
        tuition = self.get_object()
        topic_id = request.data.get("topic_id")

        if not request.user.tutor:
            raise PermissionDenied("Only tutor can access this endpoint")

        if request.user != tuition.tutor:
            raise PermissionDenied(
                "Only the tutor who created the topic can mark it as complete"
            )

        progress, _ = Progress.objects.get_or_create(
            student=request.user, tuition=tuition
        )
        topic = Topic.objects.get(id=topic_id, tuition=tuition)
        progress.completed_topics.add(topic)
        progress.save()
        serializer = ProgressSerializer(progress)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="assignment")
    def add_assignment(self, request, pk=None):
        tuition = self.get_object()
        if tuition.tutor != request.user:
            return Response(
                {"error": "Only tutor can add assignments"},
                status=status.HTTP_403_FORBIDDEN,
            )

        title = request.data.get("title")
        description = request.data.get("description", "")
        assignment = Assignment.objects.create(
            tuition=tuition, title=title, description=description
        )
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)
