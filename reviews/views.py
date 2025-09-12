from reviews.serializers import ReviewSerializers
from reviews.models import Review
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from applications.models import Application


def perform_review(self,request,tuition):
    if request.method == "GET":
        reviews = Review.objects.filter(tuition=tuition)
        return ReviewSerializers(reviews, many=True).data

    if request.method == "POST":
        if not self.request.user.is_student:
            raise PermissionDenied("Only students can leave reviews.")

        if not Application.objects.filter(tuition=tuition, user=request.user, is_selected=True).exists():
            raise PermissionDenied("This tutor doesnt tutioned you")

        serializer = ReviewSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, tuition=tuition)
        return serializer.data,status.HTTP_201_CREATED