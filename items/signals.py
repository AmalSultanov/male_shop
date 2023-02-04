from django.db.models.signals import pre_save
from django.dispatch import receiver
from items.models import ItemModel


@receiver(pre_save, sender=ItemModel)
def update_price(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.real_price = instance.price - (instance.price * instance.discount) / 100
    else:
        instance.real_price = instance.price
