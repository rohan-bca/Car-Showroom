from django.db import models
from django.contrib.auth.models import User


class CarModel(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.IntegerField()
    model_year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.brand} {self.name} | {self.model_year} | ₹{self.price}"


class CarRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    nearest_showroom = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.car_name}"

