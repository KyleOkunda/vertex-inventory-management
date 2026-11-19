from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import make_password, check_password
from .models import VertexUsers
from.utils import generate_tokens
import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.

def redirect_to_login(request):
    return redirect("login")

def login_handler(request):
    if request.method == "GET":       
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
            user = VertexUsers.objects.get(email=email)            
            user_password = user.user_password
            user_role = user.user_role
            user_id = user.user_id
            if(check_password(password, "bcrypt_sha256$" + user_password)):
                tokens = generate_tokens(user_id, user_role)

                #Set a cookie for the access token
                response = JsonResponse({"message": "Login successful", "code": "LOGIN_SUCCESS",}, status=200)
                response.set_cookie("access_token", tokens["access_token"], 60*10, secure=os.getenv("IS_PRODUCTION") == "True", httponly=True)
                response.set_cookie("refresh_token", tokens["refresh_token"], 60*60, secure=os.getenv("IS_PRODUCTION") == "True", httponly=True)
                return response
            else:
                return JsonResponse({"message": "Invalid email or password", "code": "INVALID_CREDENTIALS"}, status=401)
                        
        except Exception as e:
            print(f"Error Occured while verifying the user password\n {e}")
            return JsonResponse({"message":"Error Occured while verifying the user password", "code": "USER_AUTH_ERROR"}, status=500)