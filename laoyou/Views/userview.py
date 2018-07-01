"""
# user.py.

# do the init
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(['POST', 'GET', 'OPTIONS'])
@csrf_exempt
def changepasswd(request):
    """changepasswd."""

    if request.method == 'GET':
        return JsonResponse({
            'err': 'wrong method'
        })

    old_passwd = request.POST.get('o_passwd', None)
    new_passwd = request.POST.get('n_passwd', None)
    new_passwd2 = request.POST.get('n_passwd2', None)

    # print(old_passwd, new_passwd, new_passwd2)

    if old_passwd is None or new_passwd is None or new_passwd2 is None \
        or new_passwd != new_passwd2:
        return JsonResponse(
            {
                'err': 'please input right message'
            }
        )

    return JsonResponse({
        'err': 'None',
        'message': 'ok'
    })
