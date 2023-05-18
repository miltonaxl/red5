import jwt
import os


def generate_token(user_id):
    payload = {"user_id": user_id}
    token = jwt.encode(payload, os.getenv(
        "TOKEN_SECRET"), algorithm="HS256")
    return token
