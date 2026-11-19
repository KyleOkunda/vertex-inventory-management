from django.urls import path
from . import views
from django.shortcuts import redirect

app_name = "vertex_dashboard"

urlpatterns = [
    path("", views.dashboard_handler, name="dashboard"),
    path("user/new/", views.new_user_handler, name="create_newUser"),
]