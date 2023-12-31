import datetime
from django.db import models
from django.core.validators import MinValueValidator

class Brand(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the name of the liquor brand.")
    website = models.URLField(help_text="The URL of the brand's website.")
    country = models.CharField(max_length=30, help_text="The country of origin of the company.")
    founded = models.DateField(default=datetime.date(2000, 1, 1))

class Liquor(models.Model):
    name = models.CharField(max_length=50)
    numberOfBottles = models.IntegerField(validators=[MinValueValidator(1)])
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name