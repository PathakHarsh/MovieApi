from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.FloatField()
    release_date = models.CharField(max_length=4)
    duration=models.CharField(max_length=8) #HH:MM:SS
    description = models.CharField(max_length=500)
    
