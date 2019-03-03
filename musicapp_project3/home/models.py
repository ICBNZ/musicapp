# models.py
from django.db import models
from django.contrib.auth.models import User


class Instrument(models.Model):
    name = models.CharField(max_length=150)
    # string displayed
    def __str__(self):
        return self.name


class Tutor(models.Model):
    profile_pic = models.ImageField(upload_to="images/", default="concert.jpg") # pip3 install pillow
    name = models.CharField(max_length=150)
    experience = models.TextField(null=True, blank=True)
    instrument_avail = models.BooleanField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    instrument = models.ForeignKey('Instrument', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, primary_key=True)

    def __str__(self):
        return self.name + ' - ' + self.instrument.name


class Student(models.Model):
    profile_pic = models.ImageField(upload_to="images/", default="concert.jpg") # pip3 install pillow
    name = models.CharField(max_length=150)
    about = models.TextField(null=True, blank=True)
    instrument_req = models.BooleanField(null=True, blank=True)
    instrument = models.ForeignKey('Instrument', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, primary_key=True)

    def __str__(self):
        return self.name + ' - ' + self.instrument.name


## Booking System

class Hour(models.Model):
    DAYS =(
    ('Mon','Monday'),
    ('Tues','Tuesday'),
    ('Wed','Wednesday'),
    ('Thurs','Thursday'),
    ('Fri','Friday'),
    ('Sat','Saturday'),
    ('Sun','Sunday',)
    )
    hour = models.CharField(max_length=8)
    day_of_week = models.CharField(choices=DAYS, max_length=10)

    def __str__(self):
        return self.day_of_week + ' ' + self.hour

class Availability(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)

    def __str__(self):
        if self.available:
            return self.hour.hour + ' ' \
                + self.hour.day_of_week + ' - Available'
        else:
            return 'Sorry no availabilities'

class Booking(models.Model):
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return ' Booked for ' + self.availability.tutor.name + \
            ' on ' + self.availability.hour.hour + ' ' + \
            self.availability.hour.day_of_week
