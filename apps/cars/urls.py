from django.urls import path

from apps.cars.api_endpoints.category.CategoryCreate.views import CategoryCreateAPIview
from apps.cars.api_endpoints.category.CategoryDetail.views import CategoryDetailAPIview
from apps.cars.api_endpoints.category.CategoryList.views import CategoryListAPIview
from apps.cars.api_endpoints.category.CategoryUpdateDestroy.views import CategoryUpdateDestroyAPIview

from apps.cars.api_endpoints.cars.CarCreate.views import CarCreateAPIview
from apps.cars.api_endpoints.cars.CarDetail.views import CarDetailAPIview
from apps.cars.api_endpoints.cars.CarList.views import CarListAPIview
from apps.cars.api_endpoints.cars.CarUpdateDestroy.views import CarUpdateDestroyAPIview


urlpatterns = [
    path('', CarListAPIview.as_view(), name='car-list'),
    path('create/', CarCreateAPIview.as_view(), name='car-create'),
    path('<int:pk>/', CarDetailAPIview.as_view(), name='car-detail'),
    path('<int:pk>/update-destroy/', CarUpdateDestroyAPIview.as_view(), name='car-update-destroy'),

    path('categories/', CategoryListAPIview.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIview.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailAPIview.as_view(), name='category-detail'),
    path('categories/<int:pk>/update-destroy/', CategoryUpdateDestroyAPIview.as_view(), name='category-update-destroy'),
]
