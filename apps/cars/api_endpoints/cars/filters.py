from django_filters import CharFilter, ChoiceFilter, FilterSet, NumberFilter
from apps.cars.models import Car

class CarFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    price_gte = NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = NumberFilter(field_name='price', lookup_expr='lte')
    year = ChoiceFilter(choices=Car.YEAR_CHOICES)
    year_gte = NumberFilter(field_name='year', lookup_expr='gte')
    year_lte = NumberFilter(field_name='year', lookup_expr='lte')
    color = ChoiceFilter(choices=Car.COLOR_CHOICES)
    
    class Meta:
        model = Car
        fields = [
            'category',
            'name',
            'price_gte',
            'price_lte',
            'year',
            'year_gte',
            'year_lte',
            'color',
        ]
    
