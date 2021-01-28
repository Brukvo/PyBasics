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
from abc import ABC, abstractmethod


class Warehouse:
    pass


class Equipment:
    def __init__(self, brand, is_inkjet, pages_bk, is_color=False, pages_cl=0):
        self.brand = brand
        self.is_inkjet = is_inkjet
        self.pages_bk = pages_bk
        self.is_color = is_color
        self.pages_cl = pages_cl


class Printer(Equipment):
    def __init__(self, brand, is_inkjet, pages_bk, dpi, is_color=False, pages_cl=0):
        Equipment.__init__(brand, is_inkjet, pages_bk, is_color=False, pages_cl=0)
        self.dpi = dpi


class Scanner(Equipment):
    def __init__(self, brand, is_inkjet, pages_bk, dpi, is_color=False, pages_cl=0):
        Equipment.__init__(brand, is_inkjet, pages_bk, is_color=False, pages_cl=0)
        self.dpi = dpi


class Copier(Equipment):
    def __init__(self):



