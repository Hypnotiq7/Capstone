from django.urls import path, include
from . import views
from django.contrib.auth import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
