"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины
полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def calc_mass(self, weight: int, thick: int):
        total = self._width * self._length * weight * thick
        return total


r = Road(1250, 10)
print(f'Ширина дорожного полотна: {r.get_width()}\n',
      f'Длина дорожного полотна: {r.get_length()}\n',
      f'Общая масса покрытия: {r.calc_mass(12, 4) / 1000} т')
