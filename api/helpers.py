from api.settings import app


def unpack_url_list(urlpatterns):
    for pattern in urlpatterns:
        if type(pattern) == list:
            unpack_url_list(pattern)
        else:
            pattern()


def prepare_routes():
    from api.urls import urlpatterns
    unpack_url_list(urlpatterns)


def path(route, view, method=None, *args, **kwargs):
    methods = {
        'GET': app.get(route, *args, **kwargs),
        'POST': app.post(route, *args, **kwargs),
        'PATCH': app.get(route, *args, **kwargs),
        'PUT': app.put(route, *args, **kwargs),
        'DELETE': app.delete(route, *args, **kwargs),
    }
    pattern =  methods.get(method, None)
    if pattern:
        return pattern(view)
    return view
