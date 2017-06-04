
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

def finder (name_dir='Migrations'):
	file_list = get_file_list(name_dir)
	while True:
		user_input = input('Введите текст(q для выхода): ').lower()
		files_with_user_text = []
		if user_input == 'q':
			break
		else:
			for file_with_text in file_list:	
				with open(file_with_text) as opened_sql_file:
					if user_input.lower() in opened_sql_file.read().lower():
						files_with_user_text.append(file_with_text)
						#print(file_with_text)
			if len(files_with_user_text) == 0:
				print('Список файлов: {0}{1}Кол-во найденных результатов: {2}{1}Совпадений с {3} не найдено! Попробуйте снова!'.format('\n'.join(file_list), '\n', len(file_list), user_input))
			else:
				file_list = files_with_user_text
				print('Список файлов: {0}{1}Кол-во найденных результатов: {2}'.format('\n'.join(file_list), '\n', len(file_list)))

chdir()
finder('Advanced Migrations')


