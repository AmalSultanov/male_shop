from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class BannerModel(models.Model):
    image = models.ImageField(upload_to='home_banners', verbose_name=_('image'))
    first_title = models.CharField(max_length=100, verbose_name=_('first_title'))
    second_title = models.CharField(max_length=100, verbose_name=_('second_title'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.second_title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class ImageModel(models.Model):
    image = models.ImageField(upload_to='about_image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
