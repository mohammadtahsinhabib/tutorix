from .models import *
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "is_tutor", "is_student"]


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "is_tutor", "is_student")

    def create(self, validated_data):
        user = super().create(validated_data)
        if user.is_tutor:
            Tutor.objects.create(user=user)
        if user.is_student:
            Student.objects.create(user=user)
        return user


class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Tutor
        fields = [
            "id",
            "user",
            "bio",
            "qualifications",
            "experience",
            "hourly_rate",
            "subjects",
        ]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "user", "institution", "class_level"]
