from django.db import models
from django.contrib.auth.models import User

# info about car
class Car (models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    reg_number = models.CharField(max_length=16) # registration number

# single ride info
class Ride (models.Model):
    car = models.ForeignKey(Car)
    driverEmail = models.EmailField()
    fromAddress = models.CharField(max_length=256)    # start address
    toAddress = models.CharField(max_length=256)      # stop address
    date = models.DateTimeField(auto_now_add=True)    # date + time

class Driver (models.Model):
    account = models.ForeignKey(User, unique=True)
    car = models.ForeignKey(Car, unique=True)