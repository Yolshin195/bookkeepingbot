import jwt


def get_exp(jwt_token: str):
    decoded_token = jwt.decode(jwt_token, algorithms=["HS256"], options={"verify_signature": False})
    return decoded_token.get('exp')
