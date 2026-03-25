# core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # This controls what columns you see in the admin list view
    list_display = ['username', 'email', 'is_user', 'is_manager', 'is_servicestaff']
    
    # This adds your custom fields to the actual user editing page
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Contact Info', {'fields': ('is_user', 'is_manager', 'is_servicestaff', 'phone_number')}),
    )

# Register your custom user and admin class
admin.site.register(CustomUser, CustomUserAdmin)