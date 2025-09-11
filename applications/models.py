from django.db import models
from users.models import CustomUser
from tuition.models import Tuition


class Application(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="applications"
    )
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, related_name="applications"
    )
    is_selected = models.BooleanField(default=False)
    applied_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ("user", "tuition")
