from pydantic import BaseModel

from service.bookkeeping_api.base_service import post


class CreateUser(BaseModel):
    id: int
    username: str


async def create_telegram_user(user_id: int, username: str, access_token: str):
    return await post("/user/create/telegram", token=access_token, json=CreateUser(
        id=user_id,
        username=username).dict())
