from django.http import HttpResponse, JsonResponse
from django.views import View
# Import user model
from django.contrib.auth.models import User

# Import authentication classes
from django.contrib.auth import authenticate


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
    # Check if user is authenticated
    user = authenticate(username='user', password='789987qwe')
    if user is not None:
        return JsonResponse({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })
    return JsonResponse({'result': 'You are not authenticated'})
    