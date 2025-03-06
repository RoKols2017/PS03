import asyncio
import requests
from bs4 import BeautifulSoup
from utils.translation import translate_to_russian

# Создаем функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаем объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляем все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы код возвращал словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщает об ошибке, но не останавливает код
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()

        # Проверяем, что данные успешно получены
        if not word_dict:
            print("Не удалось получить слово. Попробуйте еще раз.")
            continue  # Начинаем следующую итерацию цикла

        word = asyncio.run(translate_to_russian(word_dict.get("english_words")))
        word_definition = asyncio.run(translate_to_russian(word_dict.get("word_definition")))

        # Начинаем игру
        print(f"Значение слова: {word_definition}")
        print(f"Подсказка: {word}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n (д/н) ")
        if play_again != "y" and play_again != "д":
            print("Спасибо за игру!")
            break

# Пример использования:
if __name__ == "__main__":
    word_game()