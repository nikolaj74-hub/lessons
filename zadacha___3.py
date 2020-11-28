class Cell:
    def __init__(self, cl):
        self.cl = cl

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cl // rows)]) + '\n' + '*' * (self.cl % rows)

    def __add__(self, other):
        return self.cl + other.cl

    def __sub__(self, other):
        return self.cl - other.cl if self.cl - other.cl > 0 \
            else 'Вычитание невозможно'

    def __mul__(self, other):
        return self.cl * other.cl

    def __floordiv__(self, other):
        return self.cl // other.cl


cell = Cell(5)
cell_2 = Cell(2)
print(cell.make_order(10), cell_2.make_order(10))
print(cell + cell_2)
print(cell * cell_2)
print(cell // cell_2)
