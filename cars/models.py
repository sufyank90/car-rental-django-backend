# cars/models.py

from django.db import models

class Car(models.Model):
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Reserved', 'Reserved'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image_url = models.URLField(max_length=200, blank=True)
    fuel = models.CharField(max_length=10, choices=FUEL_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
