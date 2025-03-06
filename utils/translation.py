from googletrans import Translator
import asyncio


async def translate_to_russian(text):
    """
    Функция переводит английский текст на русский язык

    :param text: str - входной текст на английском языке
    :return: str - переведенный текст на русском языке
    """
    translator = Translator()
    try:
        translation = await translator.translate(text, src='en', dest='ru')
        return translation.text
    except Exception as e:
        return f"Ошибка перевода: {e}"


# Пример использования:
if __name__ == "__main__":
    english_text = "Hello, how are you?"
    russian_text =  asyncio.run(translate_to_russian(english_text))
    print(russian_text)  # Вывод: "Привет, как ты?"