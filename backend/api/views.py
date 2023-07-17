import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    print(request.GET)
    try:
        data = json.loads(request.body)
    except:
        pass
    print(data)
    print(data.keys())
    data['params'] = dict(request.GET)
    data['headers'] =request.headers
    data['content_type'] =request.content_type

    print(data)
    return JsonResponse({"message":"Hi! This your Django API"})