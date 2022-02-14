

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Dealers_Form(models.Model):
    
    username = models.CharField(blank=True, max_length=50)
    name = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    contact = models.IntegerField(blank=True)
    nature_of_material = models.CharField(blank=True, max_length=50)
    weight_of_material = models.IntegerField(blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)


    def __str__(self):
        return self.email

class Drivers_Form(models.Model):

    username = models.CharField(blank=True, max_length=50)
    name = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    age = models.IntegerField(blank=True)
    contact = models.IntegerField(blank=True)
    
    truck_number = models.CharField(blank=True, max_length=16)
    truck_capacity = models.IntegerField(blank=True)
    transporter_name = models.CharField(blank=True, max_length=50)
    driving_experience = models.IntegerField(blank=True)
  
    city1 = models.CharField(blank=True, max_length=20)
    state1 = models.CharField(blank=True, max_length=20)
    city2 = models.CharField(blank=True, max_length=20)
    state2 = models.CharField(blank=True, max_length=20)
    city3 = models.CharField(blank=True, max_length=20)
    state3 = models.CharField(blank=True, max_length=20)


    def __str__(self):
        return self.transporter_name

        