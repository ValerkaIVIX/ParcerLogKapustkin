import os
import re


def ReadFile(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line)
    return data


def SearchError(log, word):
    filteredLog = [x for x in log if re.search(word, x)]
    return filteredLog


log = ReadFile(input('Введите путь до файла:'))
errorLog = SearchError(log, input('Введите слово для поиска:'))
print(*errorLog, sep='\n')
