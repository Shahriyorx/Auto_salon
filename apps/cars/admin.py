from django.contrib import admin
from apps.cars.models import Car, Category

admin.site.register(Category)
admin.site.register(Car)
