class Matrix:
    def __init__(self, matrix):  # создаем конструктор
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'  #применяем lambda  преобр.элементов списка matrix
    # в строку с разделителем '  '

    def __add__(self, other):
        return Matrix(map(lambda r, r1: map(lambda x, y: x + y, r, r1), self.matrix, other.matrix))


mm_1 = Matrix([[1, 2, 3], [4, 5, 6]])
mm_2 = Matrix([[3, 2, 1], [6, 5, 4]])
print(mm_1)
print(mm_2)

print(mm_1 + mm_2)
