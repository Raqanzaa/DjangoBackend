from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'social_provider']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_picture', 'social_provider', 'social_uid')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)