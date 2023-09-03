from typing import TypeVar, Generic, Type, Optional

import aiohttp
from pydantic import parse_obj_as

from config import BOOKKEEPING_API_HOST

ResponseType = TypeVar('ResponseType')


class UnauthorizedException(Exception):
    pass


async def post(path: str,
               response_type: Optional[Type[ResponseType]] = None,
               data: Optional[dict] = None,
               json: Optional[dict] = None,
               token: Optional[str] = None) -> ResponseType:
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'

    async with aiohttp.ClientSession() as session:
        async with session.post(f'{BOOKKEEPING_API_HOST}{path}', data=data, json=json, headers=headers) as resp:
            if resp.status != 200:
                raise UnauthorizedException

            if response_type:
                response = await resp.json()
                return parse_obj_as(response_type, response)

            return None
