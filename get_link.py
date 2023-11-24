import urllib.request

import re
import requests

# Обозначаем, что хотим получить HTML
st_accept = "text/html"

# Указываем вид запроса через брузаер Mozilla с Mac
st_useragent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 "
                "Safari/605.1.15")

# Формируем хеш заголовка для запроса
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}


# Генерируем filename из ссылки
def filename(qwert):
    result = re.search("[0-9]+\S[0-9]+\.[0-9]+\.pdf", qwert)
    result = str(result.group(0))
    result = result.replace("/", ".")
    return result


# Сохранение pdf файлов
def get_links():
    # Отправляем запрос
    req = requests.get("https://ciur.ru/ipek/DocLib61/Forms/AllItems.aspx", headers)

    # Передаем HTML в переменную
    src = req.text

    # Ищем в HTML ссылки на загрузку .pdf
    link1 = list(set(re.findall("/ipek/SiteAssets/[A-Za-z0-9]+/[A-Za-z0-9]+/[0-9]+/[0-9]+/[0-9]+.[0-9]+.pdf", src)))
    link2 = list(
        set(re.findall("/ipek/SiteAssets/[A-Za-z0-9]+/[A-Za-z0-9]+/[0-9]+/[0-9]+/[0-9]+\S[0-9]+.[0-9]+.pdf", src)))
    links = link1 + link2
    print(links)
    return links


