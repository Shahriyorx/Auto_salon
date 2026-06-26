from rest_framework import generics

from apps.cars.models import Category
from apps.cars.api_endpoints.category.CategoryDetail.serializers import CategoryDetailSerializer


class CategoryDetailAPIview(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
