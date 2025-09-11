from reviews.models import Review
from rest_framework import serializers
from users.serializers import UserSerializer


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "user", "rating", "comment", "created_at"]
        read_only_fields = ["id", "user", "created_at"]

    user = UserSerializer(read_only=True)
