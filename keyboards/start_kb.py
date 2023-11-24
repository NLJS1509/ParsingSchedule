from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расписание занятий 📅", callback_data="schedule")],
        [InlineKeyboardButton(text="Получать рассылку ❌", callback_data="newsletter_no")],
        [InlineKeyboardButton(text="Пожертвовать на хостинг 💵", callback_data="donate")]
    ]
)