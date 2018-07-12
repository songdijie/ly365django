"""
# views.py.

# implent the laoyou views
"""
# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from .serializers import BlogSerializer, UserSerializer, UserInfoSerializer
from .serializers import CommunitySerializer, TopicSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .models import Community, Topic
from .models import UserInfo

from .Views.userview import *

# permission checklist
from rest_framework import permissions


class UserInfoList(generics.ListAPIView):
    """UserInfo List."""

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class UserInfoDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    """UserInfo Detail."""

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )

    def custom_get_object(self, pk):
        """get_object."""
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404

    def update(self, request, *args, **kwargs):
        """update."""
        print(args)
        print(kwargs)
        print(request.data)
        pk = kwargs.get('pk', None)
        userinfo = self.custom_get_object(pk)
        if request.data.get('avatar', None) is None:
            request.data['avatar'] = userinfo.get('avatar', None)
        serializer = UserInfoSerializer(userinfo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UserList(generics.ListAPIView):
    """
    UserList.

    #
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class UserDetail(generics.RetrieveAPIView):
    """
    UserDetail.

    #
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class CommunityList(generics.ListAPIView):
    """
    ForumList.

    #
    """

    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class CommunityDetail(generics.RetrieveAPIView):
    """
    CommunityDetail.

    #
    """

    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class TopicList(generics.ListAPIView):
    """
    TopicList.

    #
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class TopicDetail(generics.RetrieveAPIView):
    """
    TopicDetail.

    #
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )


class BlogList(APIView):
    """
    List all Posts, or create a new post.

    detail:
    """

    queryset = Blog.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )

    def get(self, request, format=None):
        """get."""
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """post."""
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    """
    BlogDetail.

    ###
    """

    queryset = Blog.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.DjangoModelPermissions,
        )

    def get_object(self, pk):
        """get_object."""
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """get."""
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """put."""
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


def CustomSerial(indata):
    """CustomSerial."""
    outdata = dict()
    if isinstance(indata, Community):
        outdata.update(id=indata.id)
        outdata.update(name=indata.name)
        outdata.update(description=indata.description)
        outdata.update(avatar=str(indata.avatar))
        outdata.update(member=indata.member)
        outdata.update(cdate=indata.cdate)
        outdata.update(mdate=indata.mdate)
    elif isinstance(indata, Topic):
        outdata.update(id=indata.id)
        outdata.update(name=indata.name)
        outdata.update(description=indata.description)
        outdata.update(avatar=indata.avatar)
        outdata.update(member=indata.member)
        outdata.update(cdate=indata.cdate)
        outdata.update(mdate=indata.mdate)
    elif isinstance(indata, Blog):
        outdata.update(id=indata.id)
        outdata.update(name=indata.name)
        outdata.update(description=indata.description)
        outdata.update(body=indata.body)
        outdata.update(cdate=indata.cdate)
        outdata.update(mdate=indata.mdate)
    else:
        pass

    return outdata


class CommunityView(View):
    """
    CommunityViewself.

    methods:
    """

    def get(self, request, *args, **kwargs):
        """get."""
        fId = kwargs.get('fId', None)
        if fId is not None:
            fId = int(fId)
            f = Community.objects.filter(id=fId)[0]
            return JsonResponse(CustomSerial(f))
        else:
            f = Community.objects.all()
            ret = dict()
            n = 0
            for m in f:
                ret[n] = CustomSerial(m)
                n = n + 1
            return JsonResponse(ret)

    def post(self, request, *args, **kwargs):
        """post."""
        pass


class TopicView(View):
    """
    TopicView.

    methods:
    """

    def get(self, request, tId, *args, **kwargs):
        """get."""
        if not isinstance(tId, int):
            return JsonResponse(None, safe=False)
        tId = int(tId)
        t = Topic.objects.filter(id=tId)
        print(t)
        return JsonResponse(CustomSerial(t))

    def post(self, request, *args, **kwargs):
        """post."""
        pass


class BlogView(View):
    """
    Laoyou.

    methods:
    """

    def get(self, request, fId, tId, blog, *args, **kwargs):
        """Get method."""
        currentblog = Blog.objects.all()[0]
        print(currentblog.body)
        test = dict()
        test.update(name=currentblog.name)
        test.update(description=currentblog.description)
        test.update(body=currentblog.body)
        test.update(cdate=currentblog.cdate)
        return JsonResponse(test)

    def post(self, request, *args, **kwargs):
        """Post method."""
        return HttpResponse("laoyou post request")
