from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.forms import ValidationError

# Create your models here.
name_validator=RegexValidator(
    regex='^[a-zA-Z]+$', 
    message='Name must contain only alphabetic characters.'
    )

def valdidateEmail(value):
    allowed_domains = ['esprit.tn', 'univ.tn', 'mit.edu']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f'Email domain must be one of the following: {", ".join(allowed_domains)}')
class User(AbstractUser):
    Role_CHOICES = [
        ('particpant', 'Participant'),
        ('committee', 'Organizing Committee'),
        ('member', 'Member'),
    ]
    user_id = models.CharField(primary_key=True, max_length=100, unique=True)
    first_name = models.CharField(max_length=30, validators=[name_validator])
    last_name = models.CharField(max_length=30, validators=[name_validator])
    email = models.EmailField(unique=True, validators=[valdidateEmail])
    role = models.CharField(max_length=50, choices=Role_CHOICES)
    nationality = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)