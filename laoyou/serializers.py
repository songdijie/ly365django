"""
# Serializers.py.

# djaongrestframework
"""
from rest_framework import serializers
from .models import Post, Topic, Forum
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    """Post Serializers."""

    class Meta:
        """Meta class."""

        model = Post
        fields = ('id', 'name', 'description', 'body', 'topic')


class UserSerializer(serializers.ModelSerializer):
    """User Serializers."""

    blogs = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        """Meta class."""

        model = User
        fields = ('id', 'username', 'blogs')


class TopicSerializer(serializers.ModelSerializer):
    """Topic Serializers."""

    class Meta:
        """Meta class."""

        model = Topic
        fields = ('id', 'name', 'description')


class ForumSerializer(serializers.ModelSerializer):
    """Forum Serializers."""

    class Meta:
        """Meta."""

        model = Forum
        fields = ('id', 'name', 'description')
