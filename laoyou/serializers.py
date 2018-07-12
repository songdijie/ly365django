"""
# Serializers.py.

# djaongrestframework
"""
from rest_framework import serializers
from .models import Community, Topic, Blog, Comment
from .models import UserInfo
from .models import (
    City, CityCommunity, CityCommunityNews, CityCommunityNewsComment)
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


class BlogSerializer(serializers.ModelSerializer):
    """Post Serializers."""

    class Meta:
        """Meta class."""

        model = Blog
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

    community = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Blog.objects.all())

    class Meta:
        """Meta class."""

        model = Topic
        fields = ('id', 'name', 'description', 'community')


class CommunitySerializer(serializers.ModelSerializer):
    """Community Serializers."""

    class Meta:
        """Meta."""

        model = Community
        fields = ('id', 'name', 'description')


class CitySerializer(serializers.ModelSerializer):
    """City Serializers."""

    communitys = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta."""

        model = City
        fields = ('id', 'name', 'description', 'communitys')


class CityCommunitySerializer(serializers.ModelSerializer):
    """CityCommunity Serializers."""

    news = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta."""

        model = CityCommunity
        fields = ('id', 'name', 'description', 'news')


class CityCommunityNewsSerializer(serializers.ModelSerializer):
    """CityCommunityNews Serializers."""

    comments = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta."""

        model = CityCommunityNews
        fields = ('id', 'name', 'body', 'comments')


class CityCommunityNewsCommentSerializer(serializers.ModelSerializer):
    """CityCommunityNewsComment Serializers."""

    class Meta:
        """Meta."""

        model = CityCommunityNewsComment
        fields = ('id', 'comment')
