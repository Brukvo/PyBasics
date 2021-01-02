# 4. Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении
# задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая
# использование цикла.

def mult_non(x: int, y: int):
    """
    Выполняет возведение положительного целого числа в отрицательную степень.
    Аналогично 1 / x^y
    :param x: целое положительное число
    :param y: целое отрицательное число, показатель степени
    :return: None
    """
    x_hard = 1
    print(f'Результат возведения числа {x} в степень {y} через **: {x ** y}')
    for _ in range(abs(y)):
        x_hard *= x
    print(f'Результат возведения числа {x} в степень {y} через цикл: {1 / x_hard}')


def parsenum(numbers):
    parsed_numbers = []
    temp_num = None
    for number in numbers:
        if number[0] == '-':
            temp_num = number[1:]
            if temp_num.isnumeric():
                temp_num = int(temp_num)
                parsed_numbers.append(temp_num - (temp_num * 2))
                break
            else:
                return None
        elif number.isnumeric():
            parsed_numbers.append(int(number))
        else:
            return None
    return parsed_numbers


raw_x = input('Введите действительное положительное число: ')
while len(raw_x) < 1:
    print('Не допускаются пустые значения.')
    raw_x = input('Введите действительное положительное число: ')

raw_y = input('Введите целое отрицательное число: ')
while len(raw_y) < 1:
    print('Не допускаются пустые значения.')
    raw_y = input('Введите целое отрицательное число: ')

nums = parsenum([raw_x, raw_y])
if nums is None:
    print('Вами были введены не числовые значения.')
elif nums[0] < 0 or nums[1] > 0:
    print('Все или одно из введённых Вами чисел не соответствуют условию задачи.')
else:
    mult_non(nums[0], nums[1])
