from django_filters.rest_framework import DjangoFilterBackend
from progress.models import Assignment
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.models import Student, Tutor, CustomUser
from users.serializers import UserSerializer, StudentSerializer, TutorSerializer
from tuition.models import Tuition
from tuition.serializers import TuitionSerializer
from applications.models import Application
from applications.serializers import ApplicationSerializer
from progress.models import Progress
from progress.serializers import AssignmentSerializer

class UserViewSet(ModelViewSet):
    http_method_names = ["get", "patch", "delete", "post"]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TutorViewSet(ModelViewSet):
    http_method_names = ["get", "patch", "delete"]
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    @action(
        detail=False,
        methods=["get", "put"],
        url_path="profile",
        permission_classes=[IsAuthenticated],
    )
    def profile(self, request):

        if not request.user.is_tutor:
            raise PermissionDenied("Only tutor can access this endpoint")

        tutor = Tutor.objects.get(user=request.user)
        if request.method == "GET":
            return Response(TutorSerializer(tutor).data)
        elif request.method == "PUT":
            serializer = TutorSerializer(tutor, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_path="my-tuitions",
        permission_classes=[IsAuthenticated],
    )
    def my_tuitions(self, request):
        if not request.user.is_tutor:
            raise PermissionDenied("Only tutor can access this endpoint")

        tuitions = Tuition.objects.filter(tutor=request.user)
        return Response(TuitionSerializer(tuitions, many=True).data)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def applicants(self, request):
        if not request.user.is_tutor:
            raise PermissionDenied("Only tutor can access this endpoint")

        applicants = Application.objects.filter(tuition__tutor=request.user)

        tuition_id = request.query_params.get("tuition_id")
        if tuition_id:
            applicants = applicants.filter(tuition_id=tuition_id)

        serializer = ApplicationSerializer(applicants, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=["get"], url_path="students-progress",permission_classes=[IsAuthenticated])
    # # @action(detail=False, methods=["get"], url_path="students-progress/(?P<student_id>[^/.]+)",permission_classes=[IsAuthenticated])
    # def students_progress(self, request, pk=None):
    #     if not request.user.is_tutor:
    #         raise PermissionDenied("Only tutor can access this endpoint")

    #     tuitions = Tuition.objects.filter(tutor=request.user)
    #     progress = Progress.objects.filter(tuition__in=tuitions)
    #     serializer = ProgressSerializer(progress, many=True)
    #     return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="students-progress",permission_classes=[IsAuthenticated])
    def students_progress(self, request, pk=None,student_id=None):
        if not request.user.is_tutor:
            raise PermissionDenied("Only tutor can access this endpoint")
        
        assignments = Assignment.objects.filter(tuition__tutor = request.user)
        student_id = request.query_params.get("student_id")
        if student_id:
            assignments = assignments.filter(student_id =  student_id)

        return Response(AssignmentSerializer(assignments,many=True).data)
        






class StudentViewSet(ModelViewSet):
    http_method_names = ["get", "patch", "delete"]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(
        detail=False,
        methods=["get", "put"],
        url_path="profile",
        permission_classes=[IsAuthenticated],
    )
    def profile(self, request):

        if not request.user.is_student:
            raise PermissionDenied("Only student can access this endpoint")

        student = Student.objects.get(user=request.user)

        if request.method == "GET":
            return Response(StudentSerializer(student).data)

        elif request.method == "PUT":
            serializer = StudentSerializer(student, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_path="applied-tuitions",
        permission_classes=[IsAuthenticated],
    )
    def applied_tuitions(self, request):

        if not request.user.is_student:
            raise PermissionDenied("Only student can access this endpoint")

        applications = Application.objects.filter(user=request.user)
        return Response(ApplicationSerializer(applications, many=True).data)

    @action(
        detail=False,
        methods=["get"],
        url_path="accepted-tuitions",
        permission_classes=[IsAuthenticated],
    )
    def accepted_tuitions(self, request):

        if not request.user.is_student:
            raise PermissionDenied("Only students can view")

        applications = Application.objects.filter(user=request.user, is_selected=True)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
