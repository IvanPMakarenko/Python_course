import os
import osa
import chardet
import re


#temps.txt
#currencies.txt
#travel.txt

def get_file_for_convertation(input_directory=os.path.abspath(os.path.dirname(__file__)), file_name='travel.txt'):
    path_for_file = os.path.join(input_directory, file_name)
    with open(path_for_file, 'rb') as file:
        file_for_convertation = file.read()
        text_format = chardet.detect(file_for_convertation)
        correct_file_for_convertation = file_for_convertation.decode(text_format['encoding'])
        return correct_file_for_convertation


def far_to_cels(temperature=247):
    URL_FAR_TO_CELS = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

    client_far_to_cels = osa.client.Client(URL_FAR_TO_CELS)

    response_far_to_cels = client_far_to_cels.service.ConvertTemp(Temperature=temperature,
                                                                  FromUnit='degreeFahrenheit',
                                                                  ToUnit='degreeCelsius')

    return response_far_to_cels

def avg_temps(input_directory, file_name):
    temps = re.findall('\d+', get_file_for_convertation(input_directory, file_name))
    far_temps = []
    for temp in temps:
        far_temps.append(int(temp))
    avg_far_temp = sum(far_temps)/len(far_temps)
    avg_cels_temp = round(far_to_cels(avg_far_temp),1)
    print('Средняя температура: {} в цельсиях'.format(avg_cels_temp))


def get_dict(input_directory, file_name):
    currencies = get_file_for_convertation(input_directory, file_name).split('\r\n')
    cur_dice = {}
    for text in currencies:
        split_text = text.split(' ')
        cur_dice[split_text[0]] = {'amount': re.sub(',', '', split_text[1]), 'val': split_text[2]}
    return  cur_dice


def cur_converter(amount=19526, fromcurrency='RUB', tocurrency='RUB'):
    URL_CUR_CONVERTER = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client_cur_converter = osa.client.Client(URL_CUR_CONVERTER)

    response_cur_converter = client_cur_converter.service.ConvertToNum(fromCurrency=fromcurrency,
                                                                       toCurrency=tocurrency,
                                                                       amount=amount,
                                                                       rounding=True)
    return response_cur_converter


def convert_jorney_cost(input_directory, file_name):
    for country, cost in get_dict(input_directory, file_name).items():
        cost_in_rub = round(cur_converter(int(cost['amount']), cost['val']))
        print('Путь {0} в валюте: {1} {2}, в рублях: {3}'.format(country, cost['amount'], cost['val'], cost_in_rub))


def length_converter(amount=123123, fromlengthunit='Miles', tolengthunit='Kilometers'):
    URL_LENGTH_CONVERTER = 'http://www.webservicex.net/length.asmx?WSDL'
    client_length_converter = osa.client.Client(URL_LENGTH_CONVERTER)

    response_cur_converter = client_length_converter.service.ChangeLengthUnit(LengthValue=amount,
                                                                              fromLengthUnit=fromlengthunit,
                                                                              toLengthUnit=tolengthunit)
    return response_cur_converter


def travel_converter(input_directory, file_name):
    common_distance = 0
    for distance in get_dict(input_directory, file_name).values():
        common_distance += float(distance['amount'])
    common_distance_km = round(length_converter(common_distance))
    print('Общий путь составит: {} километров'.format(common_distance_km))


def homework_function():
    input_directory = input('Введите путь к директории с файлом-источником (необязательный параметр): ')
    file_name = input('Введите имя файла(temps.txt, currencies.txt, travel.txt) ').lower()
    if file_name == 'temps.txt':
        avg_temps(input_directory, file_name)
    elif file_name == 'currencies.txt':
        convert_jorney_cost(input_directory, file_name)
    elif file_name == 'travel.txt':
        travel_converter(input_directory, file_name)

homework_function()