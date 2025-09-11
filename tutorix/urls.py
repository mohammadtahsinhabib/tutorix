from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import home


schema_view = get_schema_view(
    openapi.Info(
        title="Tutorix API",
        default_version="v1",
        description="The Tuition Media API allows developers to manage students, tutors, tuition , and educational media resources such as videos, documents, and interactive lessons.It is designed for online tutoring platforms where tutors can upload content and students can access them.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@tutorix.org"),
        license=openapi.License(name="GPL v3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + debug_toolbar_urls()
