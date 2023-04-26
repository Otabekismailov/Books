from django.db.models import Count, Sum
from account.models import User
from . import models
from .models import Cart


def site_settings_context(request):
    count = models.Product.objects.all().filter(wishlist__user_id=request.user.id).aggregate(Count('count'))
    cart = models.Cart.objects.all().filter(user_id=request.user.id)
    cart_count = models.Cart.objects.all().filter(user_id=request.user.id).aggregate(
        Count('product_id'))
    cart_total_summa = models.Cart.objects.values('product__price').filter(
        user_id=request.user.id).aggregate(
        Sum('product__price'))
    cart_item = models.Cart.objects.all().values('product_id')
    product = models.Product.objects.all()
    return {
        "menu": models.CategoryMolla.objects.all(),
        "count": count['count__count'],
        "cart_count": cart_count['product_id__count'],
        "cart": cart,
        "cart_item": cart_item,
        "product": product,
        "cart_total_summa": cart_total_summa['product__price__sum'],
    }
