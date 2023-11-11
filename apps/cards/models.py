from django.db import models
from django.db.models import Avg
from apps.users import models as user_models
from apps.cards.constans import RATING

class Category(models.Model):
    title = models.CharField(null=True, max_length=100, verbose_name='Названия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='subcategories', verbose_name='Категория')
    title = models.CharField(max_length=100, verbose_name="Названия")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Под категории"
        verbose_name_plural = "Под категории"

class Product(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    subcategory = models.ManyToManyField(SubCategory, verbose_name="Категории")
    rating = models.IntegerField(choices=RATING, default=0)

    @property
    def average_rating(self):
        average = Product.objects.aggregate(avg_rating=Avg('rating')).get('avg_rating') or 0
        return min(5, max(0, average))
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class UserFavoriteProduct(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"

    def __str__(self):
        user_full_name = self.user.get_full_name()
        return f"{user_full_name} - {self.product.title}"

class Cart(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

