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
        r'^api/$', PostList.as_view()
    ),
    url(
        r'^api/(?P<pk>[0-9]+)/$', PostDetail.as_view()
    ),
    url(
        r'^api/user/$', UserList.as_view()
    ),
    url(
        r'^api/user/(?P<pk>[0-9]+)/$', UserDetail.as_view()
    ),
    url(
        r'^api/userinfo/$', UserInfoList.as_view()
    ),
    url(
        r'^api/userinfo/(?P<pk>[0-9]+)/$', UserInfoDetail.as_view()
    )
])

urlpatterns = format_suffix_patterns(urlpatterns)
