from django.db import models
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
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(SubCategory, verbose_name="Категории")
    rating = models.IntegerField(choices=RATING, default=1)

    @property
    def average_rating(self):
        ratings = [product.rating for product in Product.objects.all()]
        ratings_count = len(ratings)

        if ratings_count > 0:
            sum_ratings = sum(ratings)
            average = sum_ratings / ratings_count
            return min(5, max(0, average))  # Ограничение значений от 0 до 5
        else:
            return 0
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

class Basket(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

    def __str__(self):
        user_full_name = self.user.get_full_name()
        return f"{user_full_name} - {self.product.title}"


