from django.urls import path, include
from tuition.views import *
from users.views import UserViewSet,TutorViewSet,StudentViewSet
from rest_framework_nested import routers
from tuition.views import TuitionViewset

router = routers.DefaultRouter()
router.register("users",UserViewSet, basename="users")
router.register("tutors",TutorViewSet, basename="tutors")
router.register("students",StudentViewSet, basename="students")

tutor_router = routers.NestedDefaultRouter(router,"tutors",lookup = "tutor")
tutor_router.register('tuitions', TuitionViewset, basename='tutors-tuitions')


# student_router = routers.NestedDefaultRouter(router,"students",lookup = "student")
# student_router.register('application', ApplicationViewset, basename='students-applications')

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(tutor_router.urls)),
    # path("", include(users.urls)),
]
