from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BrandModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class ItemTagModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('item tag')
        verbose_name_plural = _('item tags')


class SizeModel(models.Model):
    title = models.CharField(max_length=3, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ColorModel(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True,
                             verbose_name=_('title'))
    code = models.CharField(max_length=15, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ItemModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'),
                                           null=True, blank=True)
    sizes = models.ManyToManyField(
        SizeModel,
        related_name='items',
        verbose_name=_('sizes')
    )
    colors = models.ManyToManyField(
        ColorModel,
        related_name='items',
        verbose_name=_('colors')
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name=_('category')
    )
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name=_('brand')
    )
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveIntegerField(default=0,
                                           verbose_name=_('discount'))
    real_price = models.FloatField(verbose_name=_('real_price'), default=0)
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextUploadingField(
        verbose_name=_('long_description'))
    tags = models.ManyToManyField(
        ItemTagModel,
        related_name='items',
        verbose_name=_('tags')
    )
    wishlist = models.ManyToManyField(
        UserModel,
        related_name='wishlist',
        verbose_name=_('wishlist')
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart')

        if cart:
            return ItemModel.objects.filter(pk__in=cart)

        return []

    def is_discount(self):
        return self.discount != 0

    def is_new(self):
        delta = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at

        return delta.days <= 3

    def get_image(self):
        images = self.images.all()

        if images:
            return self.images.first().image.url

        return '/static/img/product/no-product-image.png'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')


class ItemImageModel(models.Model):
    image = models.ImageField(upload_to='items', verbose_name=_('image'))
    item = models.ForeignKey(
        ItemModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('item')
    )

    def __str__(self):
        return self.item.title

    class Meta:
        verbose_name = _('item image')
        verbose_name_plural = _('item images')
