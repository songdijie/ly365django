# -*- conding: utf-8 -*-
"""
# models.py.
# implent the class: Forum, Topic, Post
"""

from django.db import models
from django.contrib.auth.models import User


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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s" % self.name