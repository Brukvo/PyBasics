"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""

import random as rnd


class Date:
    
    def __init__(self, raw_date: str):
        self.src_date = raw_date
        self.date = self.parse_date(self.src_date)

    @classmethod
    def parse_date(cls, raw_date):
        print(cls.__name__, ' ', end='')
        raw_day, raw_month, raw_year = raw_date.split('-')
        parsed_date = [
            int(raw_day) if raw_day.isnumeric() else 0,
            int(raw_month) if raw_month.isnumeric() else 0,
            int(raw_year) if raw_month.isnumeric() else 0
            ]
        return parsed_date

    @staticmethod
    def validate_date(parsed_date):
        day, month, year = parsed_date
        if day < 1:
            print('Число меньше диапазона 1-31. Устанавливаем в 1.')
            day = 1
        elif day > 31:
            print('Число больше диапазона 1-31. Устанавливаем в 31.')
            day = 31

        if month < 1:
            print('Месяц меньше диапазона 1-12. Устанавливаем в 1.')
            month = 1
        elif month > 12:
            print('Месяц больше диапазона 1-12. Устанавливаем 12.')
            month = 12

        if not year:
            print('Устанавливаем 2021 год.')

        return [str(day), str(month), str(year)]


for _ in range(3):
    raw = [str(rnd.randrange(1, 31)),
           str(rnd.randrange(1, 12)),
           str(rnd.randrange(1970, 2021))]
    src_date = '-'.join(raw)
    date = Date(src_date)
    validated_date = date.validate_date(date.date)

    print('.'.join(validated_date))

date2 = Date('53-13-1970')
validated_date2 = date2.validate_date(date2.date)
print('.'.join(validated_date2))

