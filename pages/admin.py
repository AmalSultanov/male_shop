from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from pages.models import BannerModel, ContactModel, ImageModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BannerModel)
class BannerModelAdmin(MyTranslationAdmin):
    list_display = ['second_title', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['first_title', 'second_title']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['created_at']
    list_filter = ['created_at']
