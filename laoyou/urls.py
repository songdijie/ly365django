"""
# urls.py.

# add the router
"""
from django.urls import path
from .views import BlogView, ForumView, TopicView

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
