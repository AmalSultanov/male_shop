from django import template
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.templatetags.static import static

from items.models import ItemModel

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang

    return '/'.join(url)


@register.simple_tag
def get_price_from(request):
    price = request.GET.get('price')
    if price:
        return price.split(';')[0]
    return 'null'


@register.simple_tag
def get_price_to(request):
    price = request.GET.get('price')
    if price:
        return price.split(';')[1]
    return 'null'


@register.simple_tag
def get_wishlist_icon(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    if request.user in item.wishlist.all():
        return static('/img/icon/new_heart.png')
    return static('/img/icon/heart.png')


@register.simple_tag
def get_wishlist_title(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    if request.user in item.wishlist.all():
        return 'remove from wishlist'
    return 'add to wishlist'


@register.filter
def in_cart(item, request):
    return item.pk in request.session.get('cart', [])


@register.simple_tag
def cart_count(request):
    return len(request.session.get('cart', []))


@register.simple_tag
def cart_sum(request):
    cart = request.session.get('cart')
    if not cart:
        return 0
    return ItemModel.get_from_cart(request).aggregate(Sum('real_price')).get('real_price__sum', 0)


@register.simple_tag
def increment_quantity(request):
    pass


@register.simple_tag
def decrement_quantity(request):
    pass
