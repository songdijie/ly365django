"""
# __init__.py.

# do the init
"""

from django import forms
from django.contrib import admin
# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from laoyou.models import Post


class PostAdminForm(forms.ModelForm):
    """PostAdminForm."""

    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        """Meta."""

        model = Post
        fields = ['name', 'description', 'body']


class PostAdmin(admin.ModelAdmin):
    """PostAdmin."""

    form = PostAdminForm


admin.site.register(Post, PostAdmin)
