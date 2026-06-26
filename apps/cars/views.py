from django.shortcuts import render

from apps.cars.models import Car

def get_products(request):
    cars = [i.to_dict() for i in Car.objects.all()]
    print(cars)