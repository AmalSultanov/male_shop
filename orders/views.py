from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from items.models import ItemModel
from orders.forms import OrderModelForm


class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'checkout.html'
    form_class = OrderModelForm
    success_message = "Successfully, wait for the call)"

    def get_success_url(self):
        return reverse('orders:history')

    def form_valid(self, form):
        items = ItemModel.get_from_cart(self.request)
        form.instance.user = self.request.user
        form.instance.price = items.aggregate(
            Sum('real_price')
        )['real_price__sum']

        order = form.save()
        order.items.set(items)

        self.request.session['cart'] = []

        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        return redirect(self.get_success_url())

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = ItemModel.get_from_cart(self.request)

        if hasattr(self.request.user, 'profile'):
            context['profile'] = self.request.user.profile

        return context


class OrderHistoryListView(LoginRequiredMixin, ListView):
    template_name = 'history.html'

    def get_queryset(self):
        return self.request.user.orders.all()
