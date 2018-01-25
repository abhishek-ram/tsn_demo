from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db.models import Avg


class Product(models.Model):
    """ Model represents a product we are selling"""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def total_ratings(self):
        return self.ratings.all().count()

    @property
    def average_rating(self):
        return self.ratings.all().aggregate(Avg('value'))['value__avg']


class Rating(models.Model):
    """ Model represents the rating given to a product"""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ratings')
    value = models.DecimalField(
        max_digits=3, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01')), MaxValueValidator(Decimal('5.00'))])
    comment = models.TextField(null=True, blank=True)
