from rest_framework import generics

from apps.cars.models import Category
from apps.cars.api_endpoints.category.CategoryList.serializers import CategoryListSerializer


class CategoryListAPIview(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
