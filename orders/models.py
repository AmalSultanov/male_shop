from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from items.models import ItemModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        related_name='orders',
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(
        ItemModel,
        related_name='orders'
    )
    price = models.FloatField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{str(self.user.profile)}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
