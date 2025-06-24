from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class House(models.Model):
    address = models.CharField(max_length=255)
    num_rooms = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='houses')
    is_available = models.BooleanField(default=True)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='tenants')

class MaintenanceRequest(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='maintenance_requests')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    