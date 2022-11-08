from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    original_price = models.FloatField()
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name
