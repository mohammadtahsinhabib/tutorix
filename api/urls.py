from django.urls import path, include
from tuition.views import *
from users.views import *
from rest_framework_nested import routers

# router = routers.DefaultRouter()
# router.register("users",CustomUserCreateSerializer, basename="users")
# router.register("tutors",CustomUserCreateSerializer, basename="tutors")
# router.register("students",CustomUserCreateSerializer, basename="students")

# tutor_router = routers.NestedDefaultRouter(router,"tutors",lookup = "tutor")
# student_router = routers.NestedDefaultRouter(router,"students",lookup = "student")



urlpatterns = [
    # path("", include(tuition.urls)),
    # path("", include(users.urls)),
]