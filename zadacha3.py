# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров
class Worker:
    def __init__(self, n, sn, pos, w, b):
        self.name = n
        self.surname = sn
        self.position = pos
        self.incom = {"wage": w, "bonus": b}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name + " " + self.surname}')

    def get_full_incom(self):
        print(f'доход ={sum(self.incom.values())} тугр.')


a = Position('коля', 'трофимов', 'слесарь', 30000, 300)
print(a.name)
print(a.incom)
print(a.surname)
print(a.position)
a.get_full_name()
a.get_full_incom()
