# core/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # The 3 Strict Roles
    is_user = models.BooleanField(default=True)           # Customer
    is_manager = models.BooleanField(default=False)       # Boss/Admin
    is_servicestaff = models.BooleanField(default=False)  # Worker
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
        
    def get_role_display(self):
        if self.is_manager: return "Manager"
        if self.is_servicestaff: return "Service Staff"
        return "User"