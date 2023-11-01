from django.db import models
from apps.cards.models import Product
# Create your models here.
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_image/')

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фотки товаров"