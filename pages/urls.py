from django.urls import path

from pages.views import (HomeTemplateView, AboutTemplateView,
                         ContactCreateView, WishlistListView, add_to_wishlist)

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist')
]
