"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост
(для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    fabric_c9n = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abstractmethod
    def calc_consumption(self):
        pass

    @staticmethod
    def calc_total_c9n():
        return sum(Clothes.fabric_c9n)


class Coat(Clothes):

    def __init__(self, name, size):
        self.v = size
        super(Coat, self).__init__(name)

    def calc_consumption(self):
        # V/6.5 + 0.5
        result = round(self.v / 6.5 + .5, 2)
        Clothes.fabric_c9n.append(result)
        return result


class Costume(Clothes):

    def __init__(self, name, height):
        self.h = height
        super(Costume, self).__init__(name)

    def calc_consumption(self):
        # 2*H + 0.3
        result = round(2 * self.h + .3, 2)
        Clothes.fabric_c9n.append(result)
        return result


c1 = Costume('Заря', 56)
c1_cons = c1.calc_consumption()
print('Костюм "{}", рост {}, расход ткани составил {} единиц'.format(c1.name, c1.h, c1_cons))

c2 = Coat('Крестьянка', 108)
c2_cons = c2.calc_consumption()
print('Пальто "{}", размер {}, расход ткани составил {} единиц'.format(c2.name, c2.v, c2_cons))

print('Итоговый расход ткани:', round(Clothes.calc_total_c9n(), 2), 'единиц')

