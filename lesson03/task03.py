# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    lst = []
    lst.append(arg1)
    lst.append(arg2)
    lst.append(arg3)
    lst.sort(reverse=True)
    max1, max2 = lst[0], lst[1]
    return max1 + max2
    
num1 = input('Введите первое число: ')
while not num1.isnumeric():
    print('Проверьте правильность ввода и попробуйте ещё раз.')
    num1 = input('Введите первое число: ')
num1 = int(num1)
    
num2 = input('Введите второе число: ')
while not num2.isnumeric():
    print('Проверьте правильность ввода и попробуйте ещё раз.')
    num2 = input('Введите второе число: ')
num2 = int(num2)

num3 = input('Введите третье число: ')
while not num3.isnumeric():
    print('Проверьте правильность ввода и попробуйте ещё раз.')
    num3 = input('Введите третье число: ')
num3 = int(num3)

print(f'Сумма двух самых больших чисел: {my_func(num1, num2, num3)}')
