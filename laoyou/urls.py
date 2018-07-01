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
from .views import ForumList, ForumDetail, TopicList, TopicDetail
from .Views.userview import changepasswd


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
        r'api/user/', UserList.as_view()
    ),
    url(
        r'api/user/<int:pk>/', UserDetail.as_view()
    ),
    url(
        r'api/userinfo/$', UserInfoList.as_view()
    ),
    url(
        r'api/userinfo/<int:pk>/', UserInfoDetail.as_view()
    ),
    url(
        r'api/userinfo/changepasswd/', changepasswd
    ),
    url(
        r'api/forum/', ForumList.as_view()
    ),
    url(
        r'api/forum/<int:pk>/', ForumDetail.as_view()
    ),
    url(
        r'api/topic/', TopicList.as_view()
    ),
    url(
        r'api/topic/<int:pk>/', TopicDetail.as_view()
    ),
    url(
        r'api/post/', PostList.as_view()
    ),
    url(
        r'api/post/<int:pk>/', PostDetail.as_view()
    )
])

urlpatterns = format_suffix_patterns(urlpatterns)
