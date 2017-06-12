# pip3 install chardet
import json
import chardet
import re
import collections
from pprint import pprint


def json_loader(user_file):
    list_name = user_file + '.json'
    with open(list_name, 'rb') as file:
        book = file.read()
        text_format = chardet.detect(book)
        print('список в кодировке: {}'.format(text_format['encoding']))
        correct_book = book.decode(text_format['encoding'])
        json_book = json.loads(correct_book)
        return json_book


def json_into_list_of_words(user_file):
    news_list = []
    for news in json_loader(user_file)['rss']['channel']['item']:
        if type(news['description']) == dict:
            new_without_symb = re.sub('<[^<]+?>', '', news['description']['__cdata']).lower()
            new_word = re.findall('\w+', new_without_symb)
        else:
            new_without_symb = re.sub('<[^<]+?>', '', news['description']).lower()
            new_word = re.findall('\w+', new_without_symb)
        news_list.extend(new_word)
    return news_list


def top10_words() -> object:
    user_file = input('Введите название файла из списка newsafr, newscy, newsit, newsfr:')
    user_top_n = int(input('Введите, какое количество популярных слов вас интересует:'))
    words_dict = {}
    rate_list = collections.Counter(json_into_list_of_words(user_file)).most_common(user_top_n)
    i = 0
    for word_position in rate_list:
        i += 1
        print('{0}. Слово "{1}" встречается в новостях {2} раз'.format(i, str(word_position[0]).upper(),
                                                                       word_position[1]))

top10_words()
