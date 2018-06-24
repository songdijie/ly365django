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

from .serializers import PostSerializer, UserSerializer, UserInfoSerializer
from .serializers import PostSerializer, UserSerializer
from .serializers import ForumSerializer, TopicSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post as Blog
from .models import Forum, Topic
from .models import UserInfo

# permission checklist
from rest_framework import permissions


class UserInfoList(generics.ListAPIView):
    """UserInfo List."""

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserInfoDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
    """UserInfo Detail."""

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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


class UserDetail(generics.RetrieveAPIView):
    """
    UserDetail.

    #
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ForumList(generics.ListAPIView):
    """
    ForumList.

    #
    """


    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class ForumDetail(generics.RetrieveAPIView):
    """
    ForumDetail.
    #
    """




class TopicList(generics.ListAPIView):
    """
    TopicList.
    #
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveAPIView):
    """
    TopicDetail.

    #
    """


    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class PostList(APIView):
    """
    List all Posts, or create a new post.

    detail:
    """

    def get(self, request, format=None):
        """get."""
        posts = Blog.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """post."""
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    PostDetail.

    ###
    """

    def get_object(self, pk):
        """get_object."""
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """get."""
        blog = self.get_object(pk)
        serializer = PostSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """put."""
        blog = self.get_object(pk)
        serializer = PostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


def CustomSerial(indata):
    """CustomSerial."""
    outdata = dict()
    if isinstance(indata, Forum):
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


class ForumView(View):
    """
    ForumViewself.

    methods:
    """

    def get(self, request, *args, **kwargs):
        """get."""
        fId = kwargs.get('fId', None)
        if fId is not None:
            fId = int(fId)
            f = Forum.objects.filter(id=fId)[0]
            return JsonResponse(CustomSerial(f))
        else:
            f = Forum.objects.all()
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
