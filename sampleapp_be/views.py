from pyramid.response import Response
from pyramid.view import view_config


# /
@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {}

# /foo
@view_config(route_name='foo', renderer='json')
def foo(request):
    return {
        'data': 'bar'
    }

# /data
@view_config(route_name='data', renderer='json', request_method='GET')
def get_data(request):
    # Add this code anywhere you need to enable CORS
    headers = (
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Credentials', 'true'),
        ('Access-Control-Allow-Headers', 'Content-Type, Authorization, x-id, Content-Length, X-Requested-With'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    )
    request.response.headerlist.extend(headers)
    return {}

