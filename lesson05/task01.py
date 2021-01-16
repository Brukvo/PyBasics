# 1. Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.
file_content, user_input = [], ''

while not user_input:
    user_input = input('Введите любые символы для записи в файл или Enter для завершения ввода: ')
    file_content.append(user_input)

with open('user_input.txt', 'a') as file:
    file.writelines(file_content)
