from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
