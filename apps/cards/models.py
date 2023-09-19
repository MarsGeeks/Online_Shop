from django.db import models

# Create your models here.
class Card(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField()
    