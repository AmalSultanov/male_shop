from modeltranslation.translator import register, TranslationOptions
from posts.models import ImageModel, AuthorModel, PostTagModel, PostModel


@register(ImageModel)
class ImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AuthorModel)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PostTagModel)
class PostTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
