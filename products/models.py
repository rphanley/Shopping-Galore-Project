"""Structure of the Product database model"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Product(models.Model):
    """fields in the Product model"""
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])

    def __str__(self):
        return self.name
