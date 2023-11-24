import os

import get_link
from main import dp, bot
from aiogram import types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import CommandStart
import urllib.request, keyboards


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(f"Привет, {msg.from_user.full_name} 👋\n"
                     f"Я - бот для получения расписания занятий 🤓", reply_markup=keyboards.main_menu)


@dp.callback_query(F.data.startswith("schedule"))
async def schedule_func(call: types.CallbackQuery):


    await call.message.edit_reply_markup()
    # links = get_link.get_links()
    #
    # # Загружаем все pdf по найденным ссылкам
    # for i in links:
    #     file_name = get_link.filename(i)
    #     link = f"https://ciur.ru/{i}"
    #     urllib.request.urlretrieve(link, file_name)
    #     document = FSInputFile(file_name)
    #     await bot.send_document(msg.from_user.id, document)
    #     os.remove(file_name)