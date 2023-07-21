from aiogram import BaseMiddleware

from API.cats import SmileApi


class WaifuApiMiddleWare(BaseMiddleware):
    """Передаёт хендлерам объект WaifuApi"""

    def __init__(self, smile_api: SmileApi):
        self.smile_api = smile_api

    async def __call__(self, handler, event, data):
        data['smile_api'] = self.smile_api
        return await handler(event, data)
