from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

schedule = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расписание на завтра", callback_data="schedule")],
        [InlineKeyboardButton(text="Расписание на сегодня", callback_data="newsletter_no")],
        [InlineKeyboardButton(text="Пожертвовать на хостинг 💵", callback_data="donate")]
    ]
)