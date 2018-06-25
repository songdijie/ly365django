"""
# admin.py.

# add the used models to the admin
"""
from django.contrib import admin
from .models import Coment
from .models import Forum, Topic, Post, UserInfo
from .models import City, CityNews, CityForum
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserInfoAdmin(admin.StackedInline):
    """
    UserInfoAdmin.

    #
    """

    model = UserInfo
    can_delete = False
    verbose_name_plural = 'user info'


class LaoyouUserAdmin(BaseUserAdmin):
    """
    LaoyouUser.

    #
    """

    inlines = (UserInfoAdmin, )


admin.site.register([Coment, ])
admin.site.register([Forum, Topic, Post, UserInfo])
admin.site.register([City, CityForum, CityNews])

admin.site.unregister(User)
admin.site.register(User, LaoyouUserAdmin)

# Register your models here.
