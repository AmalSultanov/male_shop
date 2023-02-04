from django import forms
from orders.models import OrderModel


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['user', 'items', 'price', 'created_at']
