from progress.models import Topic, Assignment, Progress
from tuition.models import Tuition
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "title", "description"]


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id", "title", "description", "created_at"]


class ProgressSerializer(serializers.ModelSerializer):
    completed_topics = TopicSerializer(many=True, read_only=True)
    assignments_completed = AssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = Progress
        fields = [
            "id",
            "student",
            "tuition",
            "completed_topics",
            "assignments_completed",
        ]


class TuitionProgressSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    assignments = AssignmentSerializer(many=True, read_only=True)
    selected_student_id = serializers.IntegerField(
        source="selected_student.id", read_only=True
    )

    class Meta:
        model = Tuition
        fields = [
            "id",
            "title",
            "description",
            "tutor",
            "selected_student_id",
            "topics",
            "assignments",
        ]
