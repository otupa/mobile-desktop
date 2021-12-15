import datetime
import pandas
import re
import os
from os.path import join, dirname, realpath

from settings import PROJECT_PATH

dataframe_list = []

def open_archive(directory, archive):
    try:
        archive_talk = open(os.path.join(
            directory, archive), 'r', encoding = 'utf-8').read().splitlines()
        name_file = archive[:-4][29:]
        return archive_talk, name_file
    except Exception as error:
        print("Erro ao abrir arquivos", error)

def line_piker(archive_talk, argument):
    return [linha for linha in archive_talk if argument in linha]

def save_csv(data_list, archive_name):
    pandas.DataFrame(data_list).to_csv(
        join(PROJECT_PATH, 'data_csv/'+archive_name+'.csv'), 
        header=False, encoding='utf-8', index=False)

def filter(argument):
    try:
        date = re.findall(r"\d+/\d+/\d+", argument)
        date = datetime.datetime.strptime(date[0], "%d/%m/%Y").strftime("%Y-%m-%d")
        if not date:
            date = dataframe_list[-1][0]
        hour = re.findall(r"\d+\:\d+", argument)
        hour = hour[0]+':00'

        date_time = "{} {}".format(date, hour)

        valor = re.findall(r"\d+\s+reais", argument)
        valor = valor[0][:-6]
        if 'desconto no boleto' in argument:
            operation = '-'
        else:
            operation = '+'

        try:
            if date_time == dataframe_list[-1][0]:
                correction = str(int(date_time[14:-3]) + 1)
                date_time_list = list(date_time)
                date_time_list[14] = correction[0]
                date_time_list[15] = correction[1]
                date_time = "".join(date_time_list)
                print(date_time, dataframe_list[-1])
        except Exception as error:
            print(error)


        format_line = [date_time, valor, operation]
        dataframe_list.append(format_line)
    except Exception as error:
        print(error, argument)
        return True



def extract(directory, arg_one, arg_two):
    for archive in os.listdir(directory):
        try:
            dataframe_list.clear()
            _open = open_archive(directory, archive)
            talk, name = _open

            fill_line = line_piker(talk, arg_one)
            filled_line = line_piker(fill_line, arg_two)
            for line in filled_line:
                filter(line)
            save_csv(dataframe_list, name)
        except Exception as error:
            print("erro ao Extrair", error,dataframe_list[-1])