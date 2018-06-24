# -*- conding: utf-8 -*-
"""
# models.py.
# implent the class: Forum, Topic, Post
"""

from django.db import models
from django.contrib.auth.models import User

class Coment(models.Model):
    """
    Coment.
    """
    body = models.CharField(max_length=100)
    cdate = models.datetime(auto_now=True)

    blog = models.ForeignKey(Post, on_delete=models.CASCADE)

class UserInfo(models.Model):
    """
    UserInfo class implent.
    property:
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.FileField(null=True, blank=True)

    def __str__(self):
        return "phone %s" % self.phone


class Forum(models.Model):
    """
    Forum class implention.
    property：
        name
        description
        avatar
        member
        cdate
        mdate
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True)
    member = models.PositiveIntegerField(null=True, blank=True, default=0)

    cdate = models.DateTimeField(auto_now=True)
    mdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

class Topic(models.Model):
    """
    Topic class implention.
    property:
        name
        description
        avatar
        member
        forum --> ForeignKey
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True)
    member = models.PositiveIntegerField(null=True, blank=True, default=0)

    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name

class Post(models.Model):
    """
    Post class implention.
    property:
        name
        description
        body
        cdate
        mdate
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    body = models.TextField(max_length=4194304) # max lenth 4MB
    cdate = models.DateTimeField(auto_now=True)
    mdate = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s" % self.name

class City(models.Model):
    """
    City class implention
    property:
    """
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=250)
    cdate = models.DateTimeField(auto_now=True)
    member = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s" % self.name


class CityNews(models.Model):
    """
    CityNews
    """
    name = models.CharField(max_length=50)
    body = models.TextField()

    city_forum = models.ForeignKey(City, on_delete=models.CASCADE)

class CityForum(models.Model):
    """
    CityForum class implention
    property:
    """
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=250)
    cdate = models.DateTimeField(auto_now=True)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name
