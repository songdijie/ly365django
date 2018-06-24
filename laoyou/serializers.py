"""
# Serializers.py.

# djaongrestframework
"""
from rest_framework import serializers
from .models import Post, Topic, Forum
from .models import UserInfo
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    """UserInfo Serializers."""

    def update(self, instance, validated_data):
        """update."""
        instance.phone = validated_data.get('phone', instance.phone)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance

    class Meta:
        """Meta class."""

        model = UserInfo
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Post Serializers."""

    class Meta:
        """Meta class."""

        model = Post
        fields = ('id', 'name', 'description', 'body', 'topic')


class UserSerializer(serializers.ModelSerializer):
    """User Serializers."""

    blogs = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta class."""

        model = User
        fields = ('id', 'username', 'blogs')


class TopicSerializer(serializers.ModelSerializer):
    """Topic Serializers."""

    forum = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Forum.objects.all())

    class Meta:
        """Meta class."""

        model = Topic
        fields = ('id', 'name', 'description', 'forum')


class ForumSerializer(serializers.ModelSerializer):
    """Forum Serializers."""

    class Meta:
        """Meta."""

        model = Forum
        fields = ('id', 'name', 'description')
