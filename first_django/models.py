from django.db import models


class CarModel(models.Model):
    brand = models.CharField(max_length=255)
    price = models.IntegerField()
    year = models.IntegerField()
