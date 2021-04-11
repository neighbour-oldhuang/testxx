from django.shortcuts import HttpResponse
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from rest_framework import views

# Create your views here.

class TestView(views.APIView):
    permission_classes= [permissions.IsAuthenticated]
    authentication_classes= (authentication.JWTAuthentication,)
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("get method")

    def post(self, request, *args, **kwargs):
        return HttpResponse('post method')
