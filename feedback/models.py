from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Feedback(models.Model):
    product = models.ForeignKey(Product)
    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.user_name
        