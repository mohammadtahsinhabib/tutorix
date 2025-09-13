from django.conf import settings
from django.db import models
from users.models import CustomUser


class Tuition(models.Model):
    tutor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="tuitions"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    class_level = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tutor.get_full_name()
