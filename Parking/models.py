# Parking/models.py
from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_user': True})
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} - {self.owner.username}"

class ServiceBooking(models.Model):
    SERVICE_CHOICES = [
        ('Storage', 'Car Storage'),
        ('PPF', 'PPF / Detailing'),
        ('Wash', 'Car Wash'),
        ('Transport', 'Shipping / Transport'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending Manager Approval'),
        ('Assigned', 'Assigned to Staff'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    
    assigned_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        limit_choices_to={'is_servicestaff': True},
        related_name='tasks'
    )
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} for {self.vehicle.license_plate}"