from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class UserViewSet(ModelViewSet):
    http_method_names = ["get","patch","delete","post"]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TutorViewSet(ModelViewSet):
    http_method_names = ["get","patch","delete","post"]
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentViewSet(ModelViewSet):
    http_method_names = ["get","patch","delete","post"]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
