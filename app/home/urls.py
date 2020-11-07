from django.urls import path;
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.login, name="login-main"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
]