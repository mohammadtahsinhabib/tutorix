from django.db import models
from tuition.models import Tuition
from django.conf import settings


class Topic(models.Model):
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, related_name="topics"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, related_name="assignments"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Progress(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="progress"
    )
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, related_name="student_progress"
    )
    completed_topics = models.ManyToManyField(Topic, blank=True)
    assignments_completed = models.ManyToManyField(Assignment, blank=True)
