from django.http import JsonResponse


def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/toket'},
        {'POST': '/api/users/toket/refresh'},
    ]

    return JsonResponse(routes, safe=False)