# File for helper functions for user login and authentication

import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from django.http import JsonResponse
from django.shortcuts import redirect

load_dotenv()
def generate_tokens(user_id, user_role):
    payload = {
        "user_id": user_id,
        "user_role": user_role
    }

    access_token = jwt.encode(payload, os.getenv("JWT_ACCESS"), algorithm="HS256")
    refresh_token = jwt.encode(payload, os.getenv("JWT_REFRESH"), algorithm="HS256")
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def authenticate_token(request):
    access_token = request.COOKIES.get("access_token")
    refresh_token = request.COOKIES.get("refresh_token")

    if not access_token or not refresh_token:
        return [False, "NO_TOKENS_PROVIDED"]

    try:
        # Decode the access token
        decoded_access_token = jwt.decode(access_token, os.getenv("JWT_ACCESS"), algorithms=["HS256"])
        return [True, decoded_access_token]
    except jwt.ExpiredSignatureError:
        # Access token has expired, try to refresh it using the refresh token
        try:
            decoded_refresh_token = jwt.decode(refresh_token, os.getenv("JWT_REFRESH"), algorithms=["HS256"])

            user_id = decoded_refresh_token["user_id"]
            user_role = decoded_refresh_token["user_role"]

            new_tokens = generate_tokens(user_id, user_role)
            new_access_token = new_tokens["access_token"]
            new_refresh_token = new_tokens["refresh_token"]
            response = JsonResponse({"message": "Access token refreshed", "code": "ACCESS_TOKEN_REFRESHED"}, status=200)
            response.set_cookie("access_token", new_access_token, 60, secure=os.getenv("IS_PRODUCTION") == "True", httponly=True)
            response.set_cookie("refresh_token", new_refresh_token, 60*10, secure=os.getenv("IS_PRODUCTION") == "True", httponly=True)
            return [True, response]
        except jwt.ExpiredSignatureError:
            return [False, "REFRESH_TOKEN_EXPIRED"]
        except jwt.InvalidTokenError:
            return [False, "INVALID_REFRESH_TOKEN"]
    except jwt.InvalidTokenError:
        return [False, "INVALID_ACCESS_TOKEN"]
