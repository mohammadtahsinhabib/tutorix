from progress.models import Assignment, Progress
from tuition.models import Tuition
from rest_framework import serializers


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        # fields = ["id", "title", "description", "created_at"]
        fields = "__all__"
        read_only_fields = ["tutor"]


class ProgressSerializer(serializers.ModelSerializer):
    # completed_topics = TopicSerializer(many=True, read_only=True)
    assignments_completed = AssignmentSerializer(many=True, read_only=True)
    assignments_given = serializers.SerializerMethodField(
        method_name="get_assignments_given"
    )

    class Meta:
        model = Progress
        fields = [
            "id",
            "student",
            "tuition",
            "assignments_given",
            "assignments_completed",
        ]

    def get_assignments_given(self, obj):
        return AssignmentSerializer(
            obj.tuition.assignments.filter(student=obj.student), many=True
        ).data


class TuitionProgressSerializer(serializers.ModelSerializer):
    # topics = TopicSerializer(many=True, read_only=True)
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
