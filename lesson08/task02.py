"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDiv(Exception):
    def __init__(self, msg):
        self.message = msg


user_input1 = input('Введите делимое: ')
while not user_input1.isnumeric():
    user_input1 = input('Введено НЕ число. Введите число: ')
user_input1 = int(user_input1)

user_input2 = input('Введите делитель: ')
while not user_input2.isnumeric():
    user_input2 = input('Введено НЕ число. Введите число: ')
try:
    user_input2 = int(user_input2)
    if user_input2 == 0:
        raise ZeroDiv('Ой! Вы ввели 0 в качестве делителя!')
except ZeroDiv as err:
    print(err)
    print('Мы добавим единицу, чтобы избежать недоразумений.')
    user_input2 += 1

print('Результат деления:', user_input1 / user_input2)
