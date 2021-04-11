from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns= [
    path(r'auth/token/obtain', TokenObtainPairView.as_view()),
    path(r'auth/token/refresh', TokenRefreshView.as_view()),
    path(r'test', views.TestView.as_view())
]