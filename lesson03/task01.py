# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
#    выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
#    обработку ситуации деления на ноль.

def divis(n1, n2):
    return n1 / n2

raw_num1 = input('Введите первое число: ')
while not raw_num1.isnumeric():
    print('Проверьте правильность ввода и попробуйте ещё раз.')
    raw_num1 = input('Введите первое число: ')
num1 = int(raw_num1)

raw_num2 = input('Введите второе число: ')
while not raw_num2.isnumeric():
    print('Проверьте правильность ввода и попробуйте ещё раз.')
    raw_num2 = input('Введите второе число: ')
num2 = int(raw_num2)

result = divis(num1, num2)
print(f'Результат деления {num1} на {num2}: {result}')
