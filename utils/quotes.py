import asyncio
from bs4 import BeautifulSoup
import requests
from utils.translation import translate_to_russian

def quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # Создаем отдельную переменную text, куда будем сохранять все цитаты
    text = soup.find_all("span", class_="text")
    # print(text)
    # создаем отдельную переменную author, куда будут сохраняться все авторы
    author = soup.find_all("small", class_="author")
    # print(author)
    # С помощью функции range(len(text)) определим общее количество цитат
    for i in range(len(text)):
        # Присваиваем номер каждой цитате так, чтобы нумерация шла с 1
        print(f"Цитата номер - {i + 1}")
        # Выводим саму цитату, указывая ее id
        print(asyncio.run(translate_to_russian(text[i].text)))
        # Выводим автора цитаты

        print(f"Автор цитаты - {asyncio.run(translate_to_russian(author[i].text))}\n")
