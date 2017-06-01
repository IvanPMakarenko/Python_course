
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path

def chdir():
	os.chdir(os.path.abspath(os.path.dirname(__file__)))

def get_file_list(name_dir):
	migrations = name_dir
	files = glob.glob(os.path.join(migrations, "*.sql"))
	return files

def finder (name_dir = 'Migrations'):
	file_list = []
	for file in get_file_list(name_dir):
		file_list.append(file)
			#print(len(file_list))

	while True:
		user_input = input('Введите текст(q для выхода): ').lower()
		file_list_2 = []
		if user_input == 'q':
			break
		else:
			for file_with_text in file_list:	
				with open(file_with_text) as f2:
					if not user_input.lower() in f2.read().lower():
						file_list_2.append(file_with_text)
						#print(file_with_text)
			file_list = list(set(file_list) - set(file_list_2))
			if len(file_list) == 0:
				file_list = file_list_2
				print(*file_list, len(file_list), sep = '\n')
				print('Совпадений не найдено, попробуйте еще раз')
			else:
				print(*file_list, len(file_list), sep = '\n')


chdir()
finder('Advanced Migrations')


