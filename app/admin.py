from django.contrib import admin
from .models import CarModel, CarRegistration
# Register your models here.


admin.site.register(CarModel)
admin.site.register(CarRegistration)