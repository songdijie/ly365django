"""
# cityview.py.

# do the cityview
"""
from django.views import View
from ..serializers import CitySerializer, CityCommunitySerializer
from ..serializers import CityCommunityNewsSerializer
from ..serializers import CityCommunityNewsCommentSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ..models import (
    City, CityCommunity, CityCommunityNews, CityCommunityNewsComment)
from rest_framework import permissions


class CityList(generics.ListAPIView):
    """City List."""

    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
    """City Detail."""

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions
    )


class CityCommunityList(generics.ListAPIView):
    """CityCommunity List."""

    queryset = CityCommunity.objects.all()
    serializer_class = CityCommunitySerializer


class CityCommunityDetail(generics.RetrieveAPIView):
    """CityCommunity Detail."""

    queryset = CityCommunity.objects.all()
    serializer_class = CityCommunitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions
    )


class CityCommunityNewsList(generics.ListAPIView):
    """CityCommunityNews List."""

    queryset = CityCommunityNews.objects.all()
    serializer_class = CityCommunityNewsSerializer


class CityCommunityNewsDetail(generics.RetrieveAPIView):
    """CityCommunityNews Detail."""

    queryset = CityCommunityNews.objects.all()
    serializer_class = CityCommunityNewsSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions
    )


class CityCommunityNewsCommentList(generics.ListAPIView):
    """CityCommunityNewsComment List."""

    queryset = CityCommunityNewsComment.objects.all()
    serializer_class = CityCommunityNewsComment


class CityCommunityNewsCommentDetail(generics.RetrieveAPIView):
    """CityCommunityNewsComment Detail."""

    queryset = CityCommunityNewsComment.objects.all()
    serializer_class = CityCommunityNewsCommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions
    )
