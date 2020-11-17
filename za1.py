from sys import argv


def zar_f():
    name, a, b, c = argv
    print('имя скрипта', name)
    print('выработка в час=', a)
    print('ставка в час=', b)
    print('премия=', c)
    s = int(a) * int(b) + int(c)
    print('зарплата=',s)
    return s


zar_f()


