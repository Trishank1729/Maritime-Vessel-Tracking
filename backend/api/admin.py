from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fullname', 'role', 'is_staff', 'created_at')
    list_filter = ('role', 'is_staff', 'created_at')
    search_fields = ('username', 'email', 'fullname')
    ordering = ('-created_at',)
    fieldsets = (
        ('Personal Info', {
            'fields': ('username', 'email', 'first_name', 'last_name', 'fullname')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Role & Timestamps', {
            'fields': ('role', 'created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
