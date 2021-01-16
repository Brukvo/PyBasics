"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки”.
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра.
"""


class Stationery:
    count = 0

    def __init__(self, title):
        self.title = title
        Stationery.count += 1

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title} буковки...')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title} человечков...')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем кистью {self.title} картину...')


general = Stationery('Конструктор')
general.draw()

pen1 = Pen('Stabilo')
pen1.draw()

pencil2 = Pencil('Koh-i-Noor')
pencil2.draw()

handle1 = Handle('Faber-Castell')
handle1.draw()

print('Всего задействовано инструментов:', Stationery.count)
