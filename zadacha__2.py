from abc import ABC, abstractmethod


class Odejka(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def p(self):
        pass
    p

    def __add__(self, other):
        return self.p + other.p


class Palto(Odejka):
    @property
    def p(self):
        print(f'{round(self.param / 6.5) + 0.5}')
        return round(self.param / 6.5) + 0.5


class Costume(Odejka):
    @property
    def p(self):
        print(f'{round(2 * self.param + 0.3) / 100}')
        return round(2 * self.param + 0.3) / 100


palt = Palto(5)
costume = Costume(6)
print(palt + costume)
