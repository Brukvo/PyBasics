# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а
# указать явно, в программе.

lst_types = [
    'string',
    2020,
    20.21,
    2+1j,
    True,
    ['element1', 'element2'],
    {'last_year': 2019, 'this_year': 2020, 'next_year': 2021},
    (23, 12),
    {23, 12, 2020, 21}
]

# Можно и так сделать :)
var_src = 5
var_lst = [str(var_src), int(var_src), float(var_src), bool(var_src)]

for lst_item in lst_types:
    print(f'Тип данных объекта со значением {lst_item} -- {type(lst_item)}')
    if type(lst_item) == 'int':
        print('Здесь мы наткнулись на целое число...')
    elif type(lst_item) == 'bool':
        print('...а здесь - на булево выражение (истина/ложь)')

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

user_list_raw = input('Введите несколько значений для списка, разделяя их запятыми без пробелов: ')
user_list = user_list_raw.split(',')

for elem in user_list:
    if user_list.index(elem) % 2:
        prev_item = user_list[user_list.index(elem) - 1]
        next_item = user_list[user_list.index(elem)]
        prev_item, next_item = next_item, prev_item
