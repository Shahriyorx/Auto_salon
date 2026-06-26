from rest_framework import generics

from apps.cars.models import Car
from apps.cars.api_endpoints.cars.CarUpdateDestroy.serializers import CarUpdateDestroySerializer

class CarUpdateDestroyAPIview(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateDestroySerializer