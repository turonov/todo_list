from django.http import HttpResponse, JsonResponse
from django.views import View
# Import user model
from django.contrib.auth.models import User

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
    