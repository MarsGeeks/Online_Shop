from django.urls import path, include

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from apps.cards.views import *

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('product/create/', ProductCreateAPIView.as_view()),
    path('product/<int:id>/', ProductDetailAPIView.as_view({'get': 'retrieve'})),
    path('favorite/', FavoriteListAPIView.as_view()),
    path("favorite/add/<int:product_id>/", AddToFavoritesAPIView.as_view()),
    path("favorite/remove/<int:product_id>/", RemoveFromFavoritesAPIView.as_view()),
    path('basket/', CartAPIView.as_view()),
    path("basket/add/<int:product_id>/", AddToCartAPIView.as_view()),
    path('basket/remove/<int:cart_item_id>/', RemoveFromCartAPIView.as_view(), name='remove_from_cart')
]
