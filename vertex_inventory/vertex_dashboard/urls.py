from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", views.dashboard_handler, name="dashboard"),
]