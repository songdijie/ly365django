"""
# views.py.

# implent the laoyou views
"""
# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post as Blog
from .models import Forum, Topic


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
