"""
# urls.py.

# add the router
"""
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogView, ForumView, TopicView
from .views import PostList, PostDetail, UserList, UserDetail
from .views import UserInfoList, UserInfoDetail
from .views import Forumlist, ForumDetail, TopicList, TopicDetail

urlpatterns = [
    path(
        'forum-<int:fId>/topic-<int:tId>/<blog>/',
        BlogView.as_view()),
    path(
        'forum/',
        ForumView.as_view()
    ),
    path(
        'forum/<fId>/',
        ForumView.as_view()
    ),
    path(
        'topic/',
        TopicView.as_view()
    ),
    path(
        'topic/<tId>/',
        TopicView.as_view()
    )
]

# restful api urls
urlpatterns.extend([
    url(
        r'^api/user/$', UserList.as_view()
    ),
    url(
        r'^api/user/(?P<pk>[0-9]+)/$', UserDetail.as_view()
    ),
    url(
        r'^api/forum/$', ForumList.as_view()
    ),
    url(
<<<<<<< HEAD
        r'^api/user/(?P<pk>[0-9]+)/$', UserDetail.as_view()
    ),
    url(
        r'^api/userinfo/$', UserInfoList.as_view()
    ),
    url(
        r'^api/userinfo/(?P<pk>[0-9]+)/$', UserInfoDetail.as_view()
=======
        r'^api/forum/(<?P<pk>[0-9]+)/$', ForumDetail.as_view()
    ),
    url(
        r'^api/topic/$', TopicList.as_view()
    ),
    url(
        r'^api/topic/(?P<pk>[0-9]+)/$', TopicDetail.as_view()
    ),
    url(
        r'^api/post/$', PostList.as_view()
    ),
    url(
        r'^api/post/(?P<pk>[0-9]+)/$', PostDetail.as_view()
>>>>>>> 91c7deb19c1c32423ebba76104d72be31bf9c43f
    )
])

urlpatterns = format_suffix_patterns(urlpatterns)
