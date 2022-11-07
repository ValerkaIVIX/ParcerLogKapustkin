import os

def ReadFile(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line)
    return data

log = ReadFile(input('Введите путь до файла:'))

print(*log, sep='\n')
