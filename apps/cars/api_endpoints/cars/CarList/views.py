from rest_framework import generics

from apps.cars.models import Car
from apps.cars.api_endpoints.cars.CarList.serializers import CarListSerializer

class CarListAPIview(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer