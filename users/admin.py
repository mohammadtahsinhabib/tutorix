from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Tutor, Student


class UserAdmin(BaseUserAdmin):
    model = CustomUser

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_tutor",
        "is_student",
        "is_staff",
    )
    list_filter = ("is_tutor", "is_student", "is_staff", "is_superuser", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_tutor",
                    "is_student",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "is_tutor",
                    "is_student",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


class TutorAdmin(admin.ModelAdmin):
    list_display = ("user", "experience", "hourly_rate", "subjects")
    search_fields = ("user__email", "user__first_name", "user__last_name", "subjects")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", "institution", "class_level")
    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "institution",
        "class_level",
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)
