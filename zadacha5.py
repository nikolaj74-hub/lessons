# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки .{self.title}')


class Pensil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки .{self.title}')


a = Pen('проверьте цвет')
a.draw()

b = Pensil('заточите карандаш')
b.draw()

c = Handle('маркер высох')
c.draw()
