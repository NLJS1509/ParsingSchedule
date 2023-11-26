from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

schedule = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расписание на сегодня ⬇️", callback_data="today")],
        [InlineKeyboardButton(text="Расписание на завтра ⤵️", callback_data="tomorrow")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
)