#pip3 install chardet
import json
import chardet
import re
from pprint import pprint


def json_loader():
	user_name = input('Введите название файла из списка newsafr, newscy, newsit, newsfr:')
	list_name = user_name + '.json'
	with open(list_name, 'rb') as f:
		book = f.read()
		text_format = chardet.detect(book)
		print('список в кодировке: {}'.format(text_format['encoding']))
		with open(list_name, encoding = text_format['encoding']) as f:
			json_book = json.load(f)
		return json_book

#print (json_loader())

def json_into_list_of_words():
	news_list = []
	for news in json_loader()['rss']['channel']['item']:
		try:
			new = news['description']['__cdata']
		except:
			new = re.sub('<br>|\n|\r',' ', re.sub('\.|[,]|[)]|[(]|!|["]','', news['description'])).strip().lower().split(' ')
		else:
			new = re.sub('<br>|\n|\r',' ', re.sub('\.|[,]|[)]|[(]|!|["]','', news['description']['__cdata'])).strip().lower().split(' ')
		news_list.extend(new)
	return news_list



def top10_words():
	user_top_n = int(input('Введите, какое количество популярных слов вас интересует:'))
	words_dict = {}
	for word in json_into_list_of_words():
		if word not in words_dict and len(word) > 2: #условие >2 для того, чтобы отсеять предлоги, тире, дефисы и т.п.
			words_dict[word] = 1
		elif word in words_dict:
			words_dict[word] += 1
	sorted_words_dict = sorted (words_dict.items(), key = lambda x:x[1], reverse=True)
	i = 0
	top_list = []
	for word in sorted_words_dict:
		i += 1
		if i <= user_top_n:
			top_list.append(word[1])
			print ('{0}. Слово "{1}" встречается в новостях {2} раз'.format(i, word[0].upper(), word[1]))
		elif word[1] in top_list and i == user_top_n + 1:
			print ('{0}. Слово "{1}" встречается в новостях {2} раз (делит последнее место)'.format(i, word[0].upper(), word[1]))
			i -= 1
		else:
			break 

top10_words()

