from django import forms
from django.contrib import admin
from import_export.admin import ImportMixin
from modeltranslation.admin import TranslationAdmin

from items.models import CategoryModel, BrandModel, ItemTagModel, ItemModel, ItemImageModel, SizeModel, ColorModel


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


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ItemTagModel)
class ItemTagModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


class ColorForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'})
        }


@admin.register(ColorModel)
class ColorModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'code']
    form = ColorForm


class ItemImageModelAdmin(admin.TabularInline):
    model = ItemImageModel


@admin.register(ItemModel)
class ItemModelAdmin(ImportMixin, MyTranslationAdmin):
    list_display = ['title', 'quantity', 'category', 'brand', 'price', 'discount', 'created_at']
    list_filter = ['category', 'quantity', 'brand', 'tags', 'created_at']
    search_fields = ['title', 'quantity', 'category__title', 'short_description', 'price']
    autocomplete_fields = ['category', 'brand', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price']

    inlines = [ItemImageModelAdmin]

    def change_view(self, request, **kwargs):
        self.exclude = ('wishlist',)
        return super().change_view(request, **kwargs)
