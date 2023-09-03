from redis_bd import read, read_access_token
from service.bookkeeping_api.auth_service import telegram_login_for_access_token, Token
from use_case.authorize_bot import authorize_bot


async def get_user_access_token(username: str) -> str:
    bot_access_token: str = await authorize_bot()
    token: Token = await telegram_login_for_access_token(username, bot_access_token)

    return token.access_token


async def authorize_user(username: str) -> str:
    return await read_access_token(f"USER-{username}", lambda: get_user_access_token(username))
