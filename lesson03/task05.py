# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
# вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

total_sum = 0


def parsenums(numbers):
    """
    Функция принимает список целых чисел, как отрицательных, так и
    положительных, в строковом представлении и возвращает их в виде целых чисел.
    :param numbers: список чисел в их строковом предствалении (напр., ['-3', 2])
    :return: список целых чисел (напр., [-3, 2])
    """
    parsed_numbers = []
    temp_num = None
    for number in numbers:
        if number[0] == '-':
            temp_num = number[1:]
            if temp_num.isnumeric():
                temp_num = int(temp_num)
                parsed_numbers.append(temp_num - (temp_num * 2))
                continue
            else:
                return None
        if number.isnumeric():
            parsed_numbers.append(int(number))
        else:
            return None
    return parsed_numbers


user_input, raw_numbers = '', []


# print(f'Сумма введёных Вами чисел: {sum(nums)}')

print("""
Введите целые (положительные и отрицательные) числа, разделённые пробелами.
Если Вы хотите прервать операцию, введите только символ =, или введите числа,
затем через пробел символ =.

""")

while True:
    while len(user_input) < 1:
        user_input = input('Ваш ряд чисел: ')
    raw_numbers = user_input.split()
    raw_numbers.sort()
    if len(raw_numbers) == 1 and raw_numbers[0] == '=':
        break
    elif len(raw_numbers) > 1 and raw_numbers[-1] == '=':
        _ = raw_numbers.pop(-1)
        nums = parsenums(raw_numbers)
        if nums is None:
            print('Не-число среди введённых Вами чисел. Завершаем работу.')
            break
        total_sum += sum(nums)
        print(f'Сумма введённых Вами чисел: {sum(nums)}')
        print(f'Общая сумма на данный момент: {total_sum}')
        print('Завершаем работу')
        break
    else:
        nums = parsenums(raw_numbers)
        if nums is None:
            print('Не-число среди введённых Вами чисел. Завершаем работу.')
            break
        total_sum += sum(nums)
        print(f'Сумма введённых Вами чисел: {sum(nums)}')
        print(f'Общая сумма на данный момент: {total_sum}')
        user_input = ''
