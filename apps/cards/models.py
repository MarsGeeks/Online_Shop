from django.db import models
from apps.users import models as user_models

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField()
    
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

class Comment(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Коментария"
        verbose_name_plural = "Коментарии"

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

