from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Tutor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor"
    )
    bio = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    experience = models.IntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    subjects = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student",
    )

    institution = models.CharField(max_length=250, blank=True)
    class_level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
