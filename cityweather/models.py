from django.db import models

# Create your models here.
class city(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    id_disable = models.BooleanField(default=False)
    
class weatherData(models.Model):
    city = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    temperature = models.FloatField() 
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    
class weatherUser(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    id_disable = models.BooleanField(default=False)