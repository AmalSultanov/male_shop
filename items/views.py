from math import ceil

from django.db.models import Q, Max, Min
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from items.models import ItemModel, CategoryModel, BrandModel, ItemTagModel, SizeModel, ColorModel


class ItemListView(ListView):
    template_name = 'items.html'
    paginate_by = 12

    def get_queryset(self):
        qs = ItemModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        price = self.request.GET.get('price')
        sort = self.request.GET.get('sort')

        if q:
            qs = qs.filter(
                Q(title__icontains=q)
            )

        if cat:
            qs = qs.filter(category__id=cat)

        if brand:
            qs = qs.filter(brand__id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if size:
            qs = qs.filter(sizes__id=size)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('-real_price')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = ItemTagModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()

        max_price, min_price = ItemModel.objects.aggregate(Max('real_price'), Min('real_price')).values()
        context['min_price'] = ceil(min_price)
        context['max_price'] = ceil(max_price)
        return context


class ItemDetailView(DetailView):
    template_name = 'item-details.html'
    model = ItemModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_goods'] = self.object.category.items.exclude(pk=self.object.pk).order_by('-pk')[:4]
        return context


class CartListView(ListView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = ItemModel.get_from_cart(self.request)

        return context

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ItemModel.objects.filter(pk__in=cart)


def add_to_cart(request, pk):
    cart = request.session.get('cart')
    if not cart:
        cart = []

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))
