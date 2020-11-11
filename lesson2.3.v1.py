while True:
    m = int(input('Введите месяц числом от 1 до 12:'))
    e = 0
    r = 12
    if m >= e or m < r:  # проверка введенного числа месяца
        a_dict = {'win': [1, 2, 12]}
        b_dict = {'spr': [3, 4, 5]}
        c_dict = {'sum': [6, 7, 8]}
        d_dict = {'aut': [9, 10, 11]}
    for v in a_dict.values():  # перебор значений в библиотеке "a_dict"
        if v.count(m) == 1:  # если количество значений "m" в библиотеке "a_dict" равно 1
            print('Зима')
        else:
            for v in b_dict.values():
                if v.count(m) == 1:
                    print('Весна')
                else:
                    for v in c_dict.values():
                        if v.count(m) == 1:
                            print('Лето')
                        else:
                            for v in d_dict.values():
                                if v.count(m) == 1:
                                    print('Осень')
                                else:
                                    print('Прошу вас от 1 до 12')
