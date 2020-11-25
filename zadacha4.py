# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, n, sp, col, d, p=True):
        self.name = n
        self.speed = sp
        self.color = col
        self.is_polise = p
        self.direction = d

    def show_speed(self):
        print(f'скорость {self.name},{self.speed}')

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self):
        print(f'машина {self.name} повернула на{self.direction} ')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает установленную скорость')
        print(f'скорость {self.name},{self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает установленную скорость')
        print(f'скорость {self.name},{self.speed}')


class PoliseCar(Car):
    def pol(self):
        if self.is_polise == True:
            print(f'это полицейская машина')


a = TownCar('lada', 80, 'зеленая', 'право')
print(a.color)
print(a.name)
a.go()
a.stop()
a.turn()
a.show_speed()

b = SportCar('corvet', 120, 'красный', 'лево')
print(b.name)
print(b.color)
b.go()
b.stop()
b.turn()
b.show_speed()

c = WorkCar('MAN', 70, 'синий', 'право')
print(c.name)
print(c.color)
c.go()
c.stop()
c.turn()
c.show_speed()

p = PoliseCar('УАЗ', 300, 'синий', '***', False)
print(p.name)
print(c.color)
p.go()
p.stop()
p.turn()
p.pol()
p.show_speed()
