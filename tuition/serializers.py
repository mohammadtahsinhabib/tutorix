from tuition.models import Tuition
from rest_framework import serializers
from users.serializers import UserSerializer


class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = "__all__"
        read_only_fields = ["tutor"]

    tutor = UserSerializer(read_only=True)
