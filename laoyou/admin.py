"""
# admin.py.

# add the used models to the admin
"""
from django.contrib import admin
from .models import Community, Topic, Comment
from .models import UserInfo
from .models import (
    City, CityCommunity, CityCommunityNews, CityCommunityNewsComment)
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .Forms.BlogAdmin import *


class UserInfoAdmin(admin.StackedInline):
    """
    UserInfoAdmin.

    #
    """

    model = UserInfo
    can_delete = False
    verbose_name_plural = '用户信息'


class LaoyouUserAdmin(BaseUserAdmin):
    """
    LaoyouUser.

    #
    """

    inlines = (UserInfoAdmin, )


admin.site.register([Comment, ])
admin.site.register([Community, Topic, UserInfo])
admin.site.register([
    City, CityCommunity, CityCommunityNews, CityCommunityNewsComment
    ])

admin.site.unregister(User)
admin.site.register(User, LaoyouUserAdmin)

# Register your models here.
