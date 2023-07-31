from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the name of the liquor brand.")
    website = models.URLField(help_text="The URL of the brand's website.")
    country = models.CharField(max_length=30, help_text="The country of origin of the company.")

class Liquor(models.Model):
    name = models.CharField(max_length=50, help_text="Bottle name")
    numberOfBottles = models.IntegerField(help_text="Number on hand")
    brand = models.CharField(max_length=50, help_text="Enter the name of the liquor brand")