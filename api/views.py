from rest_framework.decorators import api_view
from rest_framework.response import Response

#Import request 
from django.http import HttpResponse, JsonResponse

def index(request):
    # Get the method
    method = request.method # GET, POST, PUT, DELETE
    # Get the body
    body = request.body # b'{"name": "John"}'
    # Get the headers
    headers = request.headers # {'Content-Type': 'application/json'}
    # Get the path
    path = request.path # /api/
    # Get the query string
    query_string = request.GET # <QueryDict: {'name': ['John']}>
    # Get the query string
    query_string = request.GET.get('name') # John
    print(f'Method: {method}')
    print(f'Body: {body}')



    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
@api_view(['GET'])
def home(request):
    # Get the query params
    query_params = request.query_params 
    # <QueryDict: >
    print(f'Query params: {query_params}')

 
  
    
    return Response({'message': 'Hello, World!'})


