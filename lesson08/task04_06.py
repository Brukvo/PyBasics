"""
1. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет
базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для
приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.

2. Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

3. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""


class Warehouse:
    count = 0

    def __init__(self, city):
        self.city = city
        Warehouse.count += 1


class Department(Warehouse):
    count = 0

    def __init__(self, city, code):
        super(Department, self).__init__(city)
        self.code = code
        Department.count += 1

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code


class Equipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model


class Printer(Equipment):
    def __init__(self, brand, model, pages_bk, speed, dpi,
                 is_inkjet=False, is_color=0):
        super(Printer, self).__init__(brand, model)
        self.dpi = dpi # плотность точек на квадратный дюйм
        self.speed = speed # средняя скорость печати страниц, стр/мин
        self.pages_bk = pages_bk # ёмкость ч/б картриджа, стр
        self.is_inkjet = is_inkjet # True: струйный, False: лазерный
        self.is_color = is_color # ёмкость цветного картриджа, 0 = не цветной


class Scanner(Equipment):
    def __init__(self, brand, model, dpi, is_color=True):
        super(Scanner, self).__init__(brand, model)
        self.dpi = dpi
        self.is_color = is_color


class Copier(Equipment):
    def __init__(self, brand, model, pages_bk, speed, dpi,
                 is_inkjet=False, is_color=0):
        super(Copier, self).__init__(brand, model)
        self.pages_bk = pages_bk
        self.speed = speed
        self.dpi = dpi
        self.is_inkjet = is_inkjet
        self.is_color = is_color

