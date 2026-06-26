from rest_framework import generics

from apps.cars.models import Category
from apps.cars.api_endpoints.category.CategoryCreate.serializers import CategoryCreateSerializer


class CategoryCreateAPIview(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
