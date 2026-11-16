# File for helper functions for user login and authentication

import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

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

