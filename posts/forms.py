from django import forms
from posts.models import CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        exclude = ['post', 'created_at']
        model = CommentModel
