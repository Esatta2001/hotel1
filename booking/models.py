from django.db import models

BASE_PRICE = 200.00

# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    price = models.FloatField(default=BASE_PRICE)
    occupied = models.BooleanField(default=False)
    oceanside = models.BooleanField(default=False)
    suite = models.BooleanField(default=False)

    def __str__(self):
        return  "Room #" + str(self.room_num)

# Created class, Employee.
class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=100)
    shift_daynight = models.BooleanField(default=False)
    employ_ID = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + self.last_name + self.shift_daynight + self.employ_ID

   class Guest(models.Model):
       MR = 'MR'
       MS = 'MS'
       DR = 'DR'
       OT = ''
       HONORIFIC_CHOICES = [
           (MR, 'Mr.'),
           (MS, 'Ms.'),
           (DR, 'Dr.'),
           (OT, '')
       ]

    honorific = models.CharField(max_length=2, choices= HONORIFIC_CHOICES, default=OT)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    vip = models.IntegerField(max_length=-1)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first + " " + self.last

    def get_absolute_url(self):
        return '/guestlist'