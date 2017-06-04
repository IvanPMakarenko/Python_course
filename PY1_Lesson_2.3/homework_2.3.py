#pip3 install chardet
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

#pprint (json_loader())

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

#pprint(json_into_list_of_words())

def top10_words():
	user_file = input('Введите название файла из списка newsafr, newscy, newsit, newsfr:')
	user_top_n = int(input('Введите, какое количество популярных слов вас интересует:'))
	words_dict = {}
	rate_list = collections.Counter(json_into_list_of_words(user_file)).most_common(user_top_n)
	i=0
	for word_position in rate_list:
		i += 1
		print('{0}. Слово "{1}" встречается в новостях {2} раз'.format(i, str(word_position[0]).upper(), word_position[1]))
	# for word in json_into_list_of_words(user_file):
	# 	if word not in words_dict: 
	# 		words_dict[word] = 1
	# 	else:
	# 		words_dict[word] += 1
	# sorted_words_dict = sorted (words_dict.items(), key = lambda x:x[1], reverse=True)
	# i = 0
	# top_list = []
	# for word in sorted_words_dict:
	# 	i += 1
	# 	if i <= user_top_n:
	# 		top_list.append(word[1])
	# 		print ('{0}. Слово "{1}" встречается в новостях {2} раз'.format(i, word[0].upper(), word[1]))
	# 	elif word[1] in top_list and i == user_top_n + 1:
	# 		print ('{0}. Слово "{1}" встречается в новостях {2} раз (делит последнее место)'.format(i, word[0].upper(), word[1]))
	# 		i -= 1
	# 	else:
	# 		break 

top10_words()


