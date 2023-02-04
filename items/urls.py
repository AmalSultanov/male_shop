from django.urls import path

from items.views import ItemListView, ItemDetailView, add_to_cart, CartListView

app_name = 'items'

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('cart/', CartListView.as_view(), name='cart'),
]
