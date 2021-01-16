"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
numbers_en = ['One', 'Two', 'Three', 'Four']
numbers_ru = ['Один', 'Два', 'Три', 'Четыре']

lines_old, lines_new = None, []
with open('numbers.txt', 'r') as file_old:
    lines_old = file_old.readlines()

for number in numbers_en:
    for line in lines_old:
        if number in line:
            lines_new.append(line.replace(number, numbers_ru[numbers_en.index(number)]))

with open('numbers_new.txt', 'a') as file_new:
    file_new.writelines(lines_new)
