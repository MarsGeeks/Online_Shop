from django.contrib import admin
from apps.cards.models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'price', 'average_rating')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'days')

class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('product', 'characteristic', 'value')

class UserFavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Characteristic)
admin.site.register(Delivery)
admin.site.register(ProductCharacteristic)
admin.site.register(UserFavoriteProduct)
admin.site.register(Cart)
admin.site.register(CartItem)
