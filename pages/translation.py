from modeltranslation.translator import register, TranslationOptions
from pages.models import BannerModel


@register(BannerModel)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('first_title', 'second_title', 'description',)
