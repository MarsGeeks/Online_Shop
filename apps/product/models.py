from django.db import models

# Create your models here.
class ProductImage(models.Model):
    photo = models.ImageField(upload_to='apps/media/image/')

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фотки товаров"