from rest_framework import generics

from apps.cars.models import Car
from apps.cars.api_endpoints.cars.CarDetail.serializers import CarDetailSerializer

class CarDetailAPIview(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer