"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""


class Date:
    
    def __init__(self, raw_date):
        self.date = raw_date
        
    
    @classmethod
    def parse_date(cls, raw_date):
        # self.day, self.month, self.year = self.date.split('-')
        print(cls.__name__)
        raw_day, raw_month, raw_year = raw_date.split('-')
        date = {
            'day': int(raw_day) if raw_day.isnumeric() else 1,
            'month': int(raw_month) if raw_month.isnumeric() else 1,
            'year': int(raw_year) if 
            }

    @staticmethod
    def validate_date(self):
        'day': int(raw_day) if raw_day.isnumeric() else 0,
        'month': int(raw_month) if raw_month.isnumeric() else 0,
        'year': int(raw_year) if raw_month.isnumeric() else 0
