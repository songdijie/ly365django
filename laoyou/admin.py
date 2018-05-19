"""
# admin.py.

# add the used models to the admin
"""
from django.contrib import admin
from .models import Forum, Topic, Post

admin.site.register([Forum, Topic, Post])

# Register your models here.
