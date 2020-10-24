from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User


option = (
        ('bamenda', 'Bamenda'),
        ('douala', 'Douala'),
        ('yaounde', 'Yaounde'),
        ('buea', 'Buea'),
        ('bafoussam', 'Bafoussam'),
        ('ngaoundere', 'Ngaoundere'),
        )
moment = (
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        )

class Registration_form(models.Model):
    
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    message = models.TextField(null=True)

    class Meta:
        verbose_name = "user"
        
    def __str__(self):
        return self.fullname

class Bus(models.Model):
    bus_type = models.CharField(max_length=50)
    bus_number = models.CharField(max_length=40)
    bus_places = models.CharField(max_length=10)
    available = models.BooleanField(default=True)

    def __str__(self):
        if self.available:
            return self.bus_type + ", " + self.bus_number + ", (available)"
        else:
            return self.bus_type + ", " + self.bus_number 

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=20, choices=option)
    destination = models.CharField(max_length=20, choices=option)
    date = models.DateField()
    time = models.CharField(max_length=20, choices=moment)
    id_number = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id_number
    class Meta:
        ordering = ['time']








        
