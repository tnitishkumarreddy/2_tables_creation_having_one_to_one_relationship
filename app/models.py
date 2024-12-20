from django.db import models

# Create your models here.

class Country(models.Model):
    country_id=models.IntegerField(max_length=10,primary_key=True)
    country_name=models.CharField(max_length=100)

class Capital(models.Model):
    country_id=models.OneToOneField(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=100)

