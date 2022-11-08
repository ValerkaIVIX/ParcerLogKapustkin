import os
import re
from tqdm import tqdm
from time import sleep

def ReadFile(file):
    data = []
    data1 = []
    with open(file, 'r') as f:
        for line in f:
            data1.append(line)
    data.append(data1)
    return data


def ReadFiles(filepath):
    data = []
    for filename in os.listdir(filepath):
        with open(filepath + "\\" + filename, 'r') as f:
            file = []
            for line in f:
                file.append(line)
            data.append(file)
    return data


def TotalRead(filepath):
    data = []
    if os.path.isfile(filepath):
        data = ReadFile(filepath)
    else:
        data = ReadFiles(filepath)
    return data


def SearchError(log, word):
    filteredLog = []
    for l in log:
        filtered = [x for x in l if re.search(word, x)]
        filteredLog.append(filtered)
    return filteredLog


def WriteFile(newlog):
    n = 0
    for l in newlog:
        n += 1
        with open('log' + str(n) + '.txt', 'w') as f:
            for line in l:
                f.write(line + '\n')


log = TotalRead(input('Введите путь до файла или папки:'))
errorLog = SearchError(log, input('Введите слово для парсинга:'))

for i in tqdm(range(0, 100), ncols = 100,
               desc ="Обработка файла"):
    sleep(.01)

WriteFile(errorLog)
isEnd = input("Успешно! \nЧтобы закрыть программу нажмите Enter")
if isEnd:
    quit()