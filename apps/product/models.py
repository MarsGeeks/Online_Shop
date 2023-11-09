from django.db import models
from apps.cards import models as cards_models
from apps.users import models as user_models
# Create your models here.
class ProductImage(models.Model):
    product = models.ForeignKey(cards_models.Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_image/')

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фотки товаров"

class Review(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    product = models.ForeignKey(cards_models.Product, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

