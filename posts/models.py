from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class ImageModel(models.Model):
    image = models.ImageField(upload_to='blog_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


class AuthorModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    image = models.ImageField(upload_to='authors', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class PostTagModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post tag')
        verbose_name_plural = _('post tags')


class PostModel(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('title'))
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name=_('author')
    )
    image = models.ImageField(upload_to='posts', verbose_name=_('image'))
    banner = models.ImageField(upload_to='banners', verbose_name=_('banner'))
    content = RichTextUploadingField(verbose_name=_('content'))
    tags = models.ManyToManyField(
        PostTagModel,
        related_name='posts',
        verbose_name=_('tags')
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'),
                              null=True, blank=True)
    phone = models.CharField(max_length=30, verbose_name=_('phone'),
                             null=True, blank=True)
    comment = models.TextField(verbose_name=_('comment'))
    post = models.ForeignKey(
        PostModel,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('post')
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
