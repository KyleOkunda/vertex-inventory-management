from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import make_password, check_password
from .models import VertexUsers

# Create your views here.

def redirect_to_login(request):
    return redirect("login")

def login_handler(request):
    if request.method == "GET":
        str = "vertex"
        hashed_str = make_password(str)
        #hashed_str = hashed_str[14:]
        print(f"Hashed string: {hashed_str}")
        return render(request, "login.html")
    elif request.method == "POST":        
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        if(email == None or password == None):
            return_data = {"message": "Email and password are required.", "code": "EMAIL_AND_PASSWORD_REQUIRED"}
            return JsonResponse(return_data, status=400)

        # Check if the email and password match the stored values
        try:
            user_password = VertexUsers.objects.get(email=email).user_password
            if(check_password(password, "bcrypt_sha256$" + user_password)):
                return JsonResponse({"message": "Login successful", "code": "LOGIN_SUCCESS"}, status=200)
            else:
                return JsonResponse({"message": "Invalid email or password", "code": "INVALID_CREDENTIALS"}, status=401)
                        
        except Exception as e:
            print(f"Error Occured while verifying the user password\n {e}")
            return JsonResponse({"message":"Error Occured while verifying the user password", "code": "USER_AUTH_ERROR"}, status=500)