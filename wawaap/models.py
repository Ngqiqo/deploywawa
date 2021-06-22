from django.db import models
from django.urls import reverse

class User(models.Model):
    name =  models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    email =  models.EmailField()
    number =  models.IntegerField()
    country =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)

    def __str__(self):
        return self.name
               

class Websites(models.Model):
    type =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.type
