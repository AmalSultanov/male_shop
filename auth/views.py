from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def password_change(request):
    messages.add_message(request, messages.INFO, _('Password changed successfully!'))
    return redirect(reverse('profile:home'))
