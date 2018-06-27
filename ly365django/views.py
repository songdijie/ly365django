"""
# views.py.

# implent the laoyou views
"""
# from django.shortcuts import render
from django.shortcuts import render


def home(request):
    """index."""
    context = {}
    context['hello'] = 'hello world'
    return render(request, 'index.html', context)
