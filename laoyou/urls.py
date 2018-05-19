"""
# urls.py.

# add the router
"""
from django.urls import path
from .views import BlogView

urlpatterns = [
    path(
        'forum-<int:fId>/topic-<int:tId>/<blog>/',
        BlogView.as_view()),
]
