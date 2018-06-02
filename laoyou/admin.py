"""
# admin.py.

# add the used models to the admin
"""
from django.contrib import admin
from .models import Forum, Topic, Post, UserInfo

admin.site.register([Forum, Topic, Post, UserInfo])

# Register your models here.
