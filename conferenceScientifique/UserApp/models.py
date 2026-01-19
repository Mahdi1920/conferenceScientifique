from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    Role_CHOICES = [
        ('particpant', 'Participant'),
        ('committee', 'Organizing Committee'),
        ('member', 'Member'),
    ]
    user_id = models.CharField(primary_key=True, max_length=100, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=Role_CHOICES)
    nationality = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)