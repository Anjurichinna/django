from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    num =models.IntegerField()
    img = models.ImageField(upload_to='pics',default=' ') 
    