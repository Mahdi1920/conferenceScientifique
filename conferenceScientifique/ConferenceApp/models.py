from django.db import models
from UserApp.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator

# Create your models here.
class Conference(models.Model):
    THEME_CHOICES = [
        ('AI', 'Artificial Intelligence'),  
        ('ML', 'Machine Learning'),
        ('DS', 'Data Science'),
        ('WD', 'Web Development'),
        ('CY', 'Cybersecurity'),    
    ]
    name = models.CharField(max_length=200,validators=[MinLengthValidator(5, "Conference name must be at least 5 characters long.")])
    theme = models.CharField(max_length=2, choices=THEME_CHOICES)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField() 
    description = models.TextField(validators=[MaxLengthValidator(300, "Description cannot exceed 300 characters."), MinLengthValidator(20, "Description must be at least 20 characters long.")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrganizerCommittee(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Submission(models.Model):
    SUBMISSION_STATUS = [
        ('PND', 'Pending'),
        ('UR', 'Under Review'), 
        ('AC', 'Accepted'),       
        ('RJ', 'Rejected'),
    ]
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    paper = models.FileField(upload_to='submissions/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    submission_date = models.DateTimeField(auto_now_add=True)
    keywords = models.CharField(max_length=200)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=3, choices=SUBMISSION_STATUS, default='PND')
    updated_at = models.DateTimeField(auto_now=True)