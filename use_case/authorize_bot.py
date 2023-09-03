from config import TELEGRAM_BOT_USERNAME, TELEGRAM_BOT_PASSWORD
from service.bookkeeping_api.auth_service import Credentials, login_for_access_token, Token
from redis_bd import read_access_token

TELEGRAM_BOT_TOKEN = "TELEGRAM_BOT_TOKEN"


async def get_access_token() -> str:
    credentials = Credentials(
        username=TELEGRAM_BOT_USERNAME,
        password=TELEGRAM_BOT_PASSWORD
    )
    token: Token = await login_for_access_token(credentials)

    return token.access_token


async def authorize_bot() -> str:
    return await read_access_token(TELEGRAM_BOT_TOKEN, get_access_token)
