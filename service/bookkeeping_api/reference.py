import aiohttp

from config import BOOKKEEPING_API_HOST


async def get_all() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BOOKKEEPING_API_HOST}/reference/category/all') as resp:
            if resp.status == 200:
                result = 'list category: '
                for category in await resp.json():
                    result += f'\n\t{category["code"]} - {category["name"]}'
                return result
            else:
                return 'Нет категорий'
