from rest_framework import generics

from apps.cars.models import Car
from apps.cars.api_endpoints.cars.CarCreate.serializers import CarCreateSerializer

class CarCreateAPIview(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer