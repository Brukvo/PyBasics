"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    park = []

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.park.append(self.name)

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Остановка!')

    def turn(self, direction='fw'):
        if direction == 'fw':
            print('Едем вперёд!')
        elif direction == 'r':
            print('Поворачиваем направо!')
        elif direction == 'l':
            print('Поворачиваем налево!')
        elif direction == 'bw':
            print('Осторожно! Задний ход!')

    def show_speed(self):
        print(f'Скорость движения {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/ч!')
            print('Текущая скорость:', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 60} км/ч!')
            print('Текущая скорость:', self.speed)


class PoliceCar(Car):
    pass


police_car = PoliceCar(176, 'серо-буро-малиновая', 'Suzuki', True)
print('Машина:', police_car.name)
police_car.go()
police_car.turn('r')
police_car.stop()
print('*'*10)
town_car = TownCar(90, 'розовая', 'Honda Octavia', False)
print('Машина:', town_car.name)
town_car.go()
town_car.show_speed()
print(f'Цвет машины {town_car.name}:', town_car.color)
print('*'*10)
work_car = WorkCar(30, 'хаки', 'Toyota MarkII', False)
print('Машина:', work_car.name)
work_car.go()
work_car.stop()
print('*'*10)
sport_car = SportCar(180, 'красный', 'Lamborghini', False)
print('Машина:', sport_car.name)
sport_car.show_speed()

print('Машины в гараже:', ', '.join(Car.park))
