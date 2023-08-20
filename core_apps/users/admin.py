from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    model = User

    list_display = [
        "pk_id",
        "id",
        "username",
        "email",
        "is_staff",
        "is_active",
    ]

    list_display_links = ["pk_id", "id", "email"]

    list_filter = ["email", "is_staff", "is_active"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("username", "password")}),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2"),
        },
    )
    search_fields = ["username", "email"]


admin.site.register(User, UserAdmin)
admin.site.site_header = "Blog API Admin"
admin.site.site_title = "Blog API Admin Site"
admin.site.index_title = "Welcome to Authors Blog API Site"
