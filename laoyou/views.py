"""
# views.py.

# implent the laoyou views
"""
# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post as Blog


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
