import requests
import os
import chardet

API_KEY = 'trnsl.1.1.20170613T151517Z.45c25f3184fa7c8c.7ac1659188824beb11730ae13513b5b648348384'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

"""
https://translate.yandex.net/api/v1.5/tr.json/translate ? 
key=<API-ключ>
 & text=<переводимый текст>
 & lang=<направление перевода>
 & [format=<формат текста>]
 & [options=<опции перевода>]
 & [callback=<имя callback-функции>]
 """


def get_file_for_translate(input_directory=os.path.abspath(os.path.dirname(__file__)), file_name='ES.txt'):
    path_for_file = os.path.join(input_directory, file_name)
    with open(path_for_file, 'rb') as file:
        file_for_translate=file.read()
        text_format = chardet.detect(file_for_translate)
        correct_file_for_translate = file_for_translate.decode(text_format['encoding'])
        return correct_file_for_translate


def get_translation_text(input_directory, file_name, from_lang, to_lang):
    text = get_file_for_translate(input_directory, file_name)
    params = dict(
        key=API_KEY,
        text=text,
        lang='{0}-{1}'.format(from_lang, to_lang),
    )

    response = requests.get(url=URL, params=params)
    return response


def check_ouput_derectory(output_directory=os.path.join(os.path.abspath(os.path.dirname(__file__)),'result')):
    try:
        os.makedirs(output_directory)
    except OSError:
        pass
    return output_directory


def create_result_file(output_directory, input_directory, file_name, output_file_name='es-ru.txt', from_lang='es', to_lang='ru'):
    path_for_output_file = os.path.join(check_ouput_derectory(output_directory), output_file_name.upper())
    resp = get_translation_text(input_directory, file_name, from_lang, to_lang)
    translated_text = resp.json()['text']
    text_encoding = ' '.join(translated_text).encode()
    text_format = chardet.detect(text_encoding)
    text_for_load = text_encoding.decode(text_format['encoding'])
    with open(path_for_output_file, 'w', encoding=text_format['encoding']) as translated_file:
        translated_file.write(text_for_load)
        print('Done!')


def translate_function():
    input_directory = input('Введите путь к директории с файлом-источником: ')
    output_directory = input('Введите путь к директории для сохранения результата: ')
    from_lang = input('Введите язык с которого нужно перевести (ES, DE, FR): ').lower()
    to_lang = input('Введите язык на который нужно перевести (RU, ES, DE, FR): ').lower()
    file_name = from_lang + '.txt'
    output_file_name = from_lang + '-' + to_lang + '.txt'
    create_result_file(output_directory, input_directory, file_name, output_file_name, from_lang, to_lang)

translate_function()
