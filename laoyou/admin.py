"""
# admin.py.

# add the used models to the admin
"""
from django.contrib import admin
from .Models.community import Community, Topic, Comment
from .Models.user import UserInfo
from .Models.city import City, CityCommunity, CityCommunityNews
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .Forms.PostAdmin import *


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
admin.site.register([City, CityCommunity, CityCommunityNews])

admin.site.unregister(User)
admin.site.register(User, LaoyouUserAdmin)

# Register your models here.
