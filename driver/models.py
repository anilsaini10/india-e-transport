from django.db import models

# Create your models here.


class Drivers(models.Model):

    name = models.CharField(blank=True, max_length=50)
    age = models.IntegerField(blank=True)
    truck_number = models.CharField(blank=True, max_length=16)
    contact = models.IntegerField(blank=True)
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

        