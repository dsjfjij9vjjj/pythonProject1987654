import aiohttp


class BaseApi:
    async def get(self, url):
        async with aiohttp.ClientSession(headers={
            'accept': '*/*'
        }) as session:
            async with session.get(url) as request:
                answer = await request.json()
                return answer
