from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView

from items.models import ItemModel
from pages.forms import ContactModelForm
from pages.models import BannerModel, ImageModel
from posts.models import PostModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = BannerModel.objects.all()
        context['items'] = ItemModel.objects.filter(discount__gt=0).order_by('-pk')[:8]
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ImageModel.objects.all()
        return context


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')

    @staticmethod
    def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def form_invalid(self, form):
        response = super(ContactCreateView, self).form_invalid(form)
        if self.is_ajax(self.request):
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            text = f'A new letter came!\nName: {obj.name}\nEmail: {obj.email}\nMessage: {obj.message}'

            send_mail(
                'Notification',
                text,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
            )

            return redirect(self.get_success_url())

        response = super(ContactCreateView, self).form_valid(form)
        if self.is_ajax(self.request):
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response


class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'
    paginate_by = 9

    def get_queryset(self):
        return self.request.user.wishlist.all()


@login_required
def add_to_wishlist(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    user = request.user

    if user in item.wishlist.all():
        item.wishlist.remove(user)
    else:
        item.wishlist.add(user)
    return redirect(request.GET.get('next', '/'))
