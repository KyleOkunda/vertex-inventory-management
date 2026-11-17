from django.shortcuts import render
from vertex_user_login.utils import authenticate_user

# Create your views here.
def dashboard_handler(request):
    authenticate_user(request)
    
    if request.method == "GET":
        return render(request, "dashboard.html")