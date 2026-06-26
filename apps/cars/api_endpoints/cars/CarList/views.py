from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend


from apps.cars.models import Car
from apps.cars.api_endpoints.cars.CarList.serializers import CarListSerializer
from apps.cars.pagination import CarLimitOffsetpagination
from apps.cars.api_endpoints.cars.filters import CarFilter

class CarListAPIview(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    pagination_class = CarLimitOffsetpagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter