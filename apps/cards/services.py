from apps.cards.models import *
from apps.cards.exceptions import AlreadyInFavoritesError, ProductNotFoundError

def get_product(subcategory=None):
    queryset = Product.objects.all()

    if subcategory:
        queryset = queryset.filter(subcategory__name=subcategory)

    return queryset

def get_favorite_product(user):
    favorites_products = UserFavoriteProduct.objects.filter(user=user)
    product_id = favorites_products.values_list('product_id', flat=True)
    product = Product.objects.filter(pk__in=product_id)
    return product

def is_event_in_favorites(user, product_id):
    try:
        favorite_product = UserFavoriteProduct.objects.get(user=user, product_id=product_id)
        return True
    except UserFavoriteProduct.DoesNotExist:
        return False


def add_product_to_favorites(user, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if not UserFavoriteProduct.objects.filter(user=user, product_id=product_id).exists():
            UserFavoriteProduct.objects.create(user=user, product=product)
            return product
        else:
            raise AlreadyInFavoritesError()
    except Product.DoesNotExist:
        raise ProductNotFoundError()

def remove_product_from_favorites(user, product_id):
    UserFavoriteProduct.objects.filter(user=user, product_id=product_id).delete()

def get_events_by_subcategory(subcategory_id):
    queryset = Product.objects.filter(subcategory__id=subcategory_id)
    return queryset
