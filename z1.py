def my_func():
    s_1 = int(input('Введите число'))
    s_2 = int(input('Введите число'))
    res = s_1 / s_2
    print(res)
    return 'Получилось!!!!!!'
try:
    print(my_func())
except ZeroDivisionError:
    print('Error')
