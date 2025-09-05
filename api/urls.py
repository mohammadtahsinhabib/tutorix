from django.urls import path, include
from tuition.views import *
from users.views import *
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("users",UserViewSet, basename="users")
router.register("tutors",TutorViewSet, basename="tutors")
router.register("students",StudentViewSet, basename="students")

# tutor_router = routers.NestedDefaultRouter(router,"tutors",lookup = "tutor")
# student_router = routers.NestedDefaultRouter(router,"students",lookup = "student")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    # path("", include(tuition.urls)),
    # path("", include(users.urls)),
]
