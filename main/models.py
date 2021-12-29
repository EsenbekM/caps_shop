from os import name
from django.db import models

# Create your models here.



class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands', null=True, blank=True)

    def __str__(self):
        return self.name

class Cap(models.Model):
    name = models.CharField(max_length=100)
    imege = models.ImageField(upload_to='caps', null=True, blank=True)
    description = models.TextField()
    price = models.FloatField() 
    size = models.ManyToManyField(Size)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 