from django.db import models
from users.models import CustomUser
from tuition.models import Tuition


class Review(models.Model):
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "tuition"]
