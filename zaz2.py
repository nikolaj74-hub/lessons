# 2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

class Error(Exception):

    def __init__(self, ch):
        self.ch = ch


try:

    delitel = int(input("Введите делитель: "))
    if delitel == 0:
        raise Error("На ноль делить не надо !")
        #создается объект
#       собственного класса-исключения. С помощью оператора raise происходит возбуждение исключения,
#       которое перехватывается во второй ветке except и присваивается переменной err."""
except ValueError:
    print("На это делить нельзя")
except Error as err:
    print(err)
else:
    print(f"допустимый делитель: {delitel}")