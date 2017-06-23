# import requests
import os
import chardet


def get_file_for_translate(input_directory=os.path.abspath(os.path.dirname(__file__)), file_name='currencies.txt'):
    path_for_file = os.path.join(input_directory, file_name)
    with open(path_for_file, 'rb') as file:
        file_for_translate = file.read()
        text_format = chardet.detect(file_for_translate)
        correct_file_for_translate = file_for_translate.decode(text_format['encoding'])
        return correct_file_for_translate


print(get_file_for_translate())
