from service.bookkeeping_api.user_service import create_telegram_user
from use_case.authorize_bot import authorize_bot


async def create_user(user_id: int, username: str):
    access_token = await authorize_bot()

    await create_telegram_user(user_id, username, access_token)

