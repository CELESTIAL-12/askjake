from django.db import models

# Create your models here.
class Movie(models.Model):
    
    des = models.CharField(max_length=10000)
    
    