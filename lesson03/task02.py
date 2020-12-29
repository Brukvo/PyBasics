# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.

def user(name, surname, birth_year, city, email, phone):
    print(f'Вас зовут {name} {surname}, Вы родилиь в {birth_year} году.',
          f'Сейчас живёте в {city}. Для связи с Вами можно как позвонить',
          f'по номеру {phone}, так и написать на почту: {email}.')

raw_name = input('Как Вас зовут? Имя: ')
raw_surname = input('Как Вас зовут? Фамилия: ')
raw_birth_year = input('Год рождения (в 4-значном формате): ')
raw_city = input('В каком городе Вы сейчас живёте? ')
raw_email = input('Введите Ваш e-mail: ')
raw_phone = input('Введите Ваш номер телефона в любом формате: ')

user(name=raw_name, surname=raw_surname, city=raw_city,
     birth_year=raw_birth_year, phone=raw_phone, email=raw_email)
