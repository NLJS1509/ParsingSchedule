from main import dp
from aiogram import types, F
import keyboards


@dp.callback_query(F.data.startswith("back"))
async def back_func(call: types.CallbackQuery):
    await call.message.edit_text(f"Привет, {call.from_user.full_name} 👋\n"
                     f"Я - бот для получения расписания занятий 🤓", reply_markup=keyboards.main_menu)