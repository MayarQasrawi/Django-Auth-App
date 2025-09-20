from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# extends Django’s default UserAdmin,
# so you keep all standard functionality (password management, permissions, etc.).
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "is_staff", "date_joined")
    search_fields = ("email", "username")
    ordering = ("email",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "bio")
