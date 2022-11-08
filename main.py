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


def WriteFile(newlog):
    with open('parced.txt', 'w') as f:
        for line in newlog:
            f.write(line + '\n')

log = ReadFile(input('Введите путь до файла:'))
errorLog = SearchError(log, input('Введите слово для поиска:'))
WriteFile(errorLog)
print(*errorLog, sep='\n')
