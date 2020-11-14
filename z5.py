def my_f():
    i = 0
    while True:
        list = input('Введите числа через пробел.Нет желания нажмите z:').split()
        for n in list:
            if n == "z":
                return i
            else:
                try:
                    i = i + int(n)
                except ValueError:
                    print('Закончить : нажмите "Z')
        print('Сумма равна',i)


print(my_f())
