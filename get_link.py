import re
import requests
import lxml
from bs4 import BeautifulSoup

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
    result = str(result.group(0)).split("/")
    print(result)
    # try:
    #     return result[1]
    # except:
    #     return result[0]


# Сохранение pdf файлов
def get_links():
    # Отправляем запрос
    global link
    req = requests.get(
        "https://ciur.ru/ipek/SiteAssets/Forms/view.aspx?RootFolder=%2fipek%2fSiteAssets%2f01%2frz%2f2023%2f11&FolderCTID=0x01200045152E237CA79E41A0BCC98B202A0455",
        headers)

    # Передаем HTML в переменную
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    a = str(soup.find_all("div", class_="ms-vb itx"))

    # Ищем в HTML ссылки на загрузку .pdf
    links = list(set(re.findall("(/ipek/SiteAssets/[0-9]+/[A-Za-z]+/[0-9]+/[0-9]+/[0-9]+\S[0-9]+.[0-9]+\.pdf|/ipek/SiteAssets/[0-9]+/[A-Za-z]+/[0-9]+/[0-9]+/[0-9]+.[0-9]+\.pdf)", a)))
    print(links)
    return links
