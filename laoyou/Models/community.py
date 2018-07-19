"""
# community.py.

# do the init for community
"""

from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    """
    Community class implention.
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
        community --> ForeignKey
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True)
    member = models.PositiveIntegerField(null=True, blank=True, default=0)

    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name

class Blog(models.Model):
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
    viewcount = models.PositiveIntegerField(default=0)

    website = models.BooleanField(default=False) # whether it is the website link

    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s,%s" % (self.id, self.name)


class Comment(models.Model):
    """
    Comment.
    """
    body = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now=True)

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
