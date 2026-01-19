from django.db import models

# Create your models here.
class Session (models.Model):
    #id = models.AutoField (primary_key=True)
    title = models.CharField (max_length=200)
    session_day = models.DateField ()
    start_time = models.TimeField ()
    end_time = models.TimeField ()
    room = models.IntegerField()
    topic = models.CharField (max_length=200)