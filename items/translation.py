from modeltranslation.translator import register, TranslationOptions
from items.models import CategoryModel, ItemTagModel, ColorModel, ItemModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ItemTagModel)
class ItemTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ColorModel)
class ColorTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ItemModel)
class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)
