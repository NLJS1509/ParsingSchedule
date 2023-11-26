from main import dp
from aiogram import types, F
import datetime, get_link, re, urllib.request, os
from aiogram.types import FSInputFile
from main import bot


@dp.callback_query(F.data.startswith("today"))
async def schedule_func(call: types.CallbackQuery):
    #Получаем ссылки на pdf
    links = get_link.get_links()

    # Получаем сегодняшнюю дату
    day = str(datetime.date.today().day)
    month = str(datetime.date.today().month)
    year = str(datetime.date.today().year)

    for i in links:
        pdf = re.search("([0-9]+/[0-9]+/[0-9]+\S[0-9]+.[0-9]+\.pdf|[0-9]+/[0-9]+/[0-9]+.[0-9]+\.pdf)", i)
        pdf_clear = str(pdf.group(0)) #filename
        pdf_year = str(pdf_clear.split("/")[0])
        pdf_month = str(pdf_clear.split("/")[1])
        pdf_day = str(pdf_clear.split("/")[2].split(".")[0])

        if pdf_year in year and pdf_month in month and pdf_day in day:
            link = f"https://ciur.ru/{i}"
            file_name = pdf_clear.replace("/", "-").split(".")[0] + ".pdf"
            urllib.request.urlretrieve(link, file_name)
            document = FSInputFile(file_name)
            await bot.send_document(call.from_user.id, document)
            os.remove(file_name)


@dp.callback_query(F.data.startswith("tomorrow"))
async def schedule_func(call: types.CallbackQuery):
    #Получаем ссылки на pdf
    links = get_link.get_links()

    # Получаем сегодняшнюю дату
    day = str(int(datetime.date.today().day) + 1)
    month = str(datetime.date.today().month)
    year = str(datetime.date.today().year)

    for i in range(len(links)):
        pdf = re.search("([0-9]+/[0-9]+/[0-9]+\S[0-9]+.[0-9]+\.pdf|[0-9]+/[0-9]+/[0-9]+.[0-9]+\.pdf)", links[i])
        pdf_clear = str(pdf.group(0)) #filename
        pdf_year = str(pdf_clear.split("/")[0])
        pdf_month = str(pdf_clear.split("/")[1])
        pdf_day = str(pdf_clear.split("/")[2].split(".")[0])

        if pdf_year in year and pdf_month in month and pdf_day in day:
            link = f"https://ciur.ru/{links[i]}"
            file_name = pdf_clear.replace("/", "-").split(".")[0] + ".pdf"
            urllib.request.urlretrieve(link, file_name)
            document = FSInputFile(file_name)
            await bot.send_document(call.from_user.id, document)
            os.remove(file_name)
        elif i == len(links) - 1:
            await call.answer("Расписание на завтра еще не выложили 🙁", show_alert=True)