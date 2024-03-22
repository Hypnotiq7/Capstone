from django.db import models

# Create your models here. 
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
    
    
    