from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    list_filter = ['country']
    search_fields = ['items']
