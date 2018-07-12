"""
# __init__.py.

# do the init
"""

from django import forms
from django.contrib import admin
# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from laoyou.models import Blog


class BlogAdminForm(forms.ModelForm):
    """PostAdminForm."""

    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        """Meta."""

        model = Blog
        fields = ['name', 'description', 'body', 'topic', 'user']


class BlogAdmin(admin.ModelAdmin):
    """PostAdmin."""

    form = BlogAdminForm


admin.site.register(Blog, BlogAdmin)
