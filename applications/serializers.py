from applications.models import Application
from rest_framework import serializers
from users.serializers import UserSerializer
from tuition.serializers import TuitionSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "tuition", "user", "is_selected", "applied_at"]
        read_only_fields = ["is_selected", "applied_at", "tuition", "user"]

    user = UserSerializer(read_only=True)
    tuition = TuitionSerializer(read_only=True)
