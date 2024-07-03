# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_active']
    list_filter = ['email', 'username', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'username')}),
    )
    search_fields = ['email', 'username']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
