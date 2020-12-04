#  Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.
# 6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП
class Storage:# склад

    def placement(self, name, count):#размещение
        self.name = name
        self.count = count
        a = {self.name: self.count}

        if self.count != str(count):

            print(f'принято{a}')
        else:
            print(f'ошибка количество только цифрами "{self.count}"!!!')

    def exstradition(self, name, count):#выдача
        self.name = name
        self.count = count
        a = {self.name: self.count}
        print(f'выдали {a}')


class Office_equipment:
    def __init__(self, model, brand, format):
        self.model = model
        self.brand = brand
        self.format = format


class Printer(Office_equipment):

    def __init__(self, model, brand, format, jet, laser, rgb, bw):
        self.jet = jet
        self.laser = laser
        self.rgb = rgb
        self.bw = bw
        super().__init__(model, brand, format)


class Scaner(Office_equipment):
    def __init__(self, model, brand, format, tab, hand):
        self.tab = tab
        self.hand = hand
        super().__init__(model, brand, format)


class Xerox(Office_equipment):
    def __init__(self, model, brend, format):
        super().__init__(model, brend, format)


a = Storage()
a.placement('printer', "j")
a.placement('scaner', 3)
a.exstradition('printer', 1)
a.exstradition('utug', 90)

