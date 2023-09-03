from typing import Callable, Awaitable, Optional

from redis import asyncio as aioredis

from config import REDIS_HOST
from service.bookkeeping_api.access_token import get_exp

redis_pool = aioredis.from_url(
    f"redis://{REDIS_HOST}:6379", encoding="utf-8", decode_responses=True
)


async def read(key: str, get_value: Callable[[], Awaitable], exp: Optional[int] = None) -> str:
    value: str = await redis_pool.get(key)

    if value:
        return value

    value = await get_value()
    await redis_pool.set(key, value)

    if exp:
        await redis_pool.expire(key, exp)

    return value


async def read_access_token(key: str, get_value: Callable[[], Awaitable]) -> str:
    value: str = await redis_pool.get(key)

    if value:
        return value

    value: str = await get_value()

    await redis_pool.set(key, value)

    await redis_pool.expireat(key, get_exp(value))

    return value
