from django.db import models
from AutoSalon.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon, 
        }
    

class Car(BaseModel):
    YEAR_CHOICES = [(year, year) for year in range(2010, 2026)]
    COLOR_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
        ('silver', 'Silver'),
        ('gray', 'Gray'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='cars',
    )
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category.to_dict(),
            'year': self.year,
            'color': self.color,
        }
