from rest_framework import generics

from apps.cars.models import Category
from apps.cars.api_endpoints.category.CategoryUpdateDestroy.serializers import CategoryUpdateDestroySerializer


class CategoryUpdateDestroyAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateDestroySerializer
