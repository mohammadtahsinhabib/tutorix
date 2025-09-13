from progress.models import Assignment
from rest_framework import serializers


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"
        read_only_fields = ["is_completed"]
