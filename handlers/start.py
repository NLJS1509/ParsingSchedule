import os

import get_link
from main import dp, bot
from aiogram import types, F

from aiogram.filters.command import CommandStart
import urllib.request, keyboards


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(f"Привет, {msg.from_user.full_name} 👋\n"
                     f"Я - бот для получения расписания занятий 🤓", reply_markup=keyboards.main_menu)


@dp.callback_query(F.data.startswith("schedule"))
async def schedule_func(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=keyboards.schedule)




@dp.callback_query(F.data.startswith("donate"))
async def donate_func(call: types.CallbackQuery):
    await call.message.edit_text("Бот разработан с целью упростить рутину.\nЯ содержу его за свой счет. Если ты пользуешься им регулярно и он тебе нравится, то буду очень благодарен за помощь.\n\n"
                                 "<code>5536 9140 9265 9964</code>\n"
                                 "<code>Александр Олегович К.</code>\n\n", parse_mode="HTML", reply_markup=keyboards.back)