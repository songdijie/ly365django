"""
# urls.py.

# add the router
"""
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogView, CommunityView, TopicView
from .views import BlogList, BlogDetail, UserList, UserDetail
from .views import UserInfoList, UserInfoDetail
from .views import CommunityList, CommunityDetail, TopicList, TopicDetail
from .Views.userview import changepasswd
from .Views.cityview import CityList, CityDetail
from .Views.cityview import CityCommunityList, CityCommunityDetail
from .Views.cityview import (
    CityCommunityNewsList,
    CityCommunityNewsDetail,
    CityCommunityNewsCommentList,
    CityCommunityNewsCommentDetail
)


urlpatterns = [
    path(
        'forum-<int:fId>/topic-<int:tId>/<blog>/',
        BlogView.as_view()),
    path(
        'forum/',
        CommunityView.as_view()
    ),
    path(
        'forum/<fId>/',
        CommunityView.as_view()
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
    path(
        r'api/user/', UserList.as_view()
    ),
    path(
        r'api/user/<int:pk>/', UserDetail.as_view()
    ),
    path(
        r'api/userinfo/', UserInfoList.as_view()
    ),
    path(
        r'api/userinfo/<int:pk>/', UserInfoDetail.as_view()
    ),
    path(
        r'api/userinfo/changepasswd/', changepasswd
    ),
    path(
        r'api/community/', CommunityList.as_view()
    ),
    path(
        r'api/community/<int:pk>/', CommunityDetail.as_view()
    ),
    path(
        r'api/topic/', TopicList.as_view()
    ),
    path(
        r'api/topic/<int:pk>/', TopicDetail.as_view()
    ),
    path(
        r'api/blog/', BlogList.as_view()
    ),
    path(
        r'api/blog/<int:pk>/', BlogDetail.as_view()
    ),
    path(
        r'api/city/', CityList.as_view()
    ),
    path(
        r'api/city/<int:pk>/', CityDetail.as_view()
    ),
    path(
        r'api/citycommunity/', CityCommunityList.as_view()
    ),
    path(
        r'api/citycommunity/<int:pk>/', CityCommunityDetail.as_view()
    ),
    path(
        r'api/citycommunitynews/', CityCommunityNewsList.as_view()
    ),
    path(
        r'api/citycommunitynews/<int:pk>/', CityCommunityNewsDetail.as_view()
    ),
    path(
        r'api/citycommunitynewscomment/',
        CityCommunityNewsCommentList.as_view()
    ),
    path(
        r'api/citycommunitynewscomment/<int:pk>/',
        CityCommunityNewsCommentDetail.as_view()
    )
])

urlpatterns = format_suffix_patterns(urlpatterns)
