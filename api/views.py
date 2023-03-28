from django.http import HttpResponse, JsonResponse
from django.views import View
# Import user model
from django.contrib.auth.models import User

# Import authentication classes
from django.contrib.auth import authenticate
from base64 import b64decode

class HomeView(View):
    def get(self, request):
        user = User.objects.all()
        data = {
            'users': []
        }
        for i in user:
            data['users'].append({
                'id': i.id,
                'username': i.username,
                'email': i.email
            })
        return JsonResponse(data)
    def post(self, request):
        return JsonResponse({'message': 'POST'})


def index(request):
    # Get headers
    auth = request.headers.get('Authorization')
    # Check if Authorization header is present
    if auth is None:
        return JsonResponse({'result': 'You are not authenticated'})
    # Get token
    token = auth.split(' ')[1]
    auth=b64decode(token).decode() # Decode token
    username, password = auth.split(':') # Split token

    # Check if user is authenticated
    
    user = authenticate(username=username, password=password)

    if user is not None:
        return JsonResponse({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })
    return JsonResponse({'result': 'You are not authenticated'})
    