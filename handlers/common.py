from API.cats import smile_api
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

common_router = Router()


@common_router.message(Command('start'))
async def handle_start(message: Message):
    await message.answer('Привет я бот который отправляет картинки котов😼😼😼😼!!!!Что бы сгенерировать кота введите: /cats  '
                         'что бы показать пасхалку от разраба введите: /love🤫🤫🤫')


@common_router.message(Command('cats'))
async def cats_start(message: Message):
    cat_URL = await smile_api.get_cats()
    await message.answer_photo(cat_URL)



@common_router.message(Command(commands='help'))
async def handle_help(message: Message):
    await message.answer('Зачем тебе помощь просто введи: /cats и будет кот!😼😼😼😼😼😼'
                         'или введи:/love для пасхали🤫🤫🤫')
@common_router.message(Command(commands='love'))
async def love_cats(message: Message):
    await message.answer('ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         'ฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅฅ^•ﻌ•^ฅ'
                         ' :Я разработчик я тебе передаю привет ')
@common_router.message(Command(commands='developer'))
async def developer_cats(message: Message):
    await message.answer('Спасибо что пользуешься моим ботом!!')
