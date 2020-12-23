# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
winter, spring, summer, autumn = [1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]
seasons = {
    'Зима': [1, 2, 12],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]
}

# Простой вариант запроса месяца:
# user_month = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))

# Более сложный - с проверкой ввода
user_month = input('Введите номер месяца в виде целого числа от 1 до 12: ')
if user_month.isdecimal():
    user_month = int(user_month)
    if 1 <= user_month <= 12:
        # Через list
        print('Решение через списки: ', end='')
        if user_month in winter:
            print('Зима')
        elif user_month in spring:
            print('Весна')
        elif user_month in summer:
            print('Лето')
        elif user_month in autumn:
            print('Осень')

        # Через dict
        print('Решение через словари: ', end='')
        for season in seasons:
            if user_month in seasons[season]:
                print(season, '- время года.')
    else:
        print('Простите, номер месяца выходит за указанные пределы.')
else:
    print('Простите, допускается только целое цисло.')


