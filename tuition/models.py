from django.db import models
from users.models import CustomUser

class Tuition(models.Model):
    tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tuitions")
    title = models.CharField(max_length=200)
    description = models.TextField()
    class_level = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
