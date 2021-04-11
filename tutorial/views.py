from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户检查或编辑api路径
    """
    queryset= User.objects.all().order_by('-date_joined')
    serializer_class= UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset= Group.objects.all()
    serializer_class= GroupSerializer