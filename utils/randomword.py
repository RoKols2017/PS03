import requests
from bs4 import BeautifulSoup

# Создаем функцию которая будет получать информацию
def get_english_words():
    url = "https://rendomword.com/"
    try:
        response = requests.get(url)
        # Создаем объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляем все пробелы из результата
        get_english_words() = soup.find("div", id="random_word").text.strip()
    except:
        print("Произошла ошибка")