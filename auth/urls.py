from django.urls import path, include
from auth.views import password_change

urlpatterns = [
    path('password/change/done/', password_change),
    path('', include('registration.backends.default.urls'))
]
