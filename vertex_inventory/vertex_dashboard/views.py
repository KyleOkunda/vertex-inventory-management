from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from vertex_user_login.utils import authenticate_token
from django.http import JsonResponse
from uuid7 import UUIDv7
from vertex_user_login.models import VertexUsers
import json



# Create your views here.
def dashboard_handler(request):
    [is_valid, response] = authenticate_token(request)
    if not is_valid:
        return redirect("vertex_user_login:login")     
    
    if request.method == "GET":
        return render(request, "dashboard.html")

def new_user_handler(request):
    [is_valid, response] = authenticate_token(request)
    if not is_valid:
            return redirect("vertex_user_login:login")

    user_id = response.get("user_id")
        
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name") 
        phone_number = data.get("phone_number")
        staff_email = data.get("staff_email")
        user_role = data.get("user_role")
        department = data.get("department")
        temporary_password = data.get("temporary_password")
        confirm_password = data.get("confirm_password")

        if(temporary_password != confirm_password):
            return JsonResponse({"message": "Passwords provided do not match"}, status=400)

        hashed_password = make_password(temporary_password)
        hashed_password = hashed_password[14:]

        print(f"First Name: {first_name}\nLast Name: {last_name}\nPhone Number: {phone_number}\nEmail: {staff_email}\nUser Role: {user_role}\nDepartment: {department}\nTemporary Password: {temporary_password}\nConfirm Password: {confirm_password}")


        # Generate a unique user ID using UUIDv7
        generated_user_id = UUIDv7()

        # Create a new user instance and save it to the database
        new_user = VertexUsers(
            user_id=generated_user_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=staff_email,
            user_role=user_role,
            position=user_role,  # Assuming position is the same as user_role for now
            department=department,
            account_created_by=user_id,
            user_password=hashed_password,
        )
        new_user.save()

        return JsonResponse({"message": "New user created successfully", "code": "USER_CREATION_SUCCESS"}, status=201)
        