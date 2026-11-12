from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def redirect_to_login(request):
    return redirect("login")

def login_handler(request):
    return render(request, "login.html")