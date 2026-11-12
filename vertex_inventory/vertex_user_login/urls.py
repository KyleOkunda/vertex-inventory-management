from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", views.redirect_to_login, name="redirect_to_login"),
    path("login/", views.login_handler, name="login"),
]