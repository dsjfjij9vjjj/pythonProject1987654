from API.base import BaseApi


class SmileApi(BaseApi):
    async def get_cats(self):
        answer = await self.get(f"https://api.thecatapi.com/v1/images/search")
        return answer[0]['url']


smile_api = SmileApi()



