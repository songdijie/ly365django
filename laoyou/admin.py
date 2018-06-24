"""
# admin.py.

# add the used models to the admin
"""
from django.contrib import admin
from .models import Coment
from .models import Forum, Topic, Post, UserInfo
from .models import City, CityNews, CityForum

admin.site.register([Coment, ])
admin.site.register([Forum, Topic, Post, UserInfo])
admin.site.register([City, CityForum, CityNews])

# Register your models here.
