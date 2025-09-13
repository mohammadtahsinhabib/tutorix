from django.urls import path, include
from tuition.views import *
from users.views import UserViewSet, TutorViewSet, StudentViewSet
from rest_framework_nested import routers
from tuition.views import TuitionViewSet
from progress.views import ProgressViewSet, AssignmentViewSet
from reviews.views import ReviewViewSet


router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("tutors", TutorViewSet, basename="tutors")
router.register("students", StudentViewSet, basename="students")
router.register("tuitions", TuitionViewSet, basename="tuitions")


tuition_router = routers.NestedDefaultRouter(router, "tuitions", lookup="tuition")
tuition_router.register("reviews", ReviewViewSet, basename="tuition-reviews")
# tuition_router.register("progress", ProgressViewSet, basename="tuition-progress")
tuition_router.register("assignments", AssignmentViewSet, basename="tuition-status")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(tuition_router.urls)),
    # path("", include(payment_router.urls)),
]
