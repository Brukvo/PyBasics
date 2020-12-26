# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#   (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
#   {
#       “название”: [“компьютер”, “принтер”, “сканер”],
#       “цена”: [20000, 6000, 2000],
#       “количество”: [5, 2, 7],
#       “ед”: [“шт.”]
#   }
ERROR_MSG = 'Ошибка при вводе данных. Попробуйте ещё раз.'

counter = 1
goods = []
analytics = {}
names_list, prices_list, qty_list, measure_list = [], [], [], []
raw_price, raw_qty = '', ''

try:
    while True:
        name = input('Введите название товара: ')
        while not raw_price.isdecimal():
            raw_price = input('Введите цену за единицу: ')
            if raw_price.isdecimal():
                price = int(raw_price)
                break
            else:
                print(ERROR_MSG)
        while not raw_qty.isdecimal():
            raw_qty = input('Введите количество на складе в виде целого числа: ')
            if raw_qty.isdecimal():
                qty = int(raw_qty)
                break
            else:
                print(ERROR_MSG)
        measure = input('Укажите единицу измерения, например, кг или г: ')
        goods.append(
            (counter, {'название': name, 'цена': price, 'количество': qty, 'ед': measure})
        )
        raw_qty, raw_price = '', ''
        counter += 1
        print('-' * 80)
        choice = input('Продолжить ввод данных? (Д/н/Y/n): ')
        if choice.lower() == 'д' or choice.lower() == 'y':
            continue
        break

    for good in goods:
        names_list.append(good[1]['название'])
        prices_list.append(good[1]['цена'])
        qty_list.append(good[1]['количество'])
        measure_list.append(good[1]['ед'])

    analytics['название'] = names_list
    analytics['цена'] = prices_list
    analytics['количество'] = qty_list
    analytics['ед'] = measure_list

    print(analytics)
except KeyboardInterrupt:
    for elem in goods:
        print(elem)

