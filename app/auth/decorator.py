import jwt
import os


def authentication_required(func):

    def wrapper(*args, **kwargs):
        token = args[1].context.headers.get("Authorization", "")
        if token.startswith("Bearer "):
            token = token.split(" ")[1]
            try:
                payload = jwt.decode(token, os.getenv(
                    "TOKEN_SECRET"), algorithms=["HS256"])
                args[1].context.user_id = payload["user_id"]
            except jwt.InvalidTokenError:
                raise Exception("Token inválido o expirado")
        else:
            raise Exception("Token es requerido")
        return func(*args, **kwargs)
    return wrapper
