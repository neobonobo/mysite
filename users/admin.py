# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,  UserProfile  # new

class UserProfileInline(admin.StackedInline):  # new
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User Profile"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
    inlines = [UserProfileInline]  # new


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)  # new
