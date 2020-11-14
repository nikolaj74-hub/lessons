# def my_funk(x, y):
#   return 1 / x ** abs(y)


# print(my_funk(x=float(input('Введите дйствительное число')), y=int(input('Введите отрицательное целое число'))))


a = lambda x, y: 1 / float(x) ** abs(int(y))
print(a(x=input("введите дйствительное число'"), y=input("Введите отрицательное целое число")))
