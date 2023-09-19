from django.contrib import admin
from apps.cards.models import *
# Register your models here.
admin.site.register(Card)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(SubCategory)
