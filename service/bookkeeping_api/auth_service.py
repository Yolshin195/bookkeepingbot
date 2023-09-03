from pydantic import BaseModel
from service.bookkeeping_api.base_service import post


class Token(BaseModel):
    access_token: str
    token_type: str


class Credentials(BaseModel):
    username: str
    password: str


async def login_for_access_token(credentials: Credentials) -> Token:
    return await post("/auth/token", Token, data=credentials.dict())


async def telegram_login_for_access_token(username: str, access_token: str) -> Token:
    return await post("/auth/telegram", Token, json={"username": username}, token=access_token)
