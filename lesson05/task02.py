"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

lines = None
with open('predefined.txt', 'r') as file:
    lines = file.readlines()

print(f'Всего строк в файле "{file.name}": {len(lines)}')
for i, line in enumerate(lines, start=1):
    print(f'Число слов в строке {i}: {len(line.split())}')
