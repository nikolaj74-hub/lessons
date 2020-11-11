while True:
    m = int(input('Введите месяц числом от 1 до 12'))
    e = 0
    r = 12
    if m >= e or m < r:
        win = [1, 2, 12]
        sprig = [3, 4, 5]
        sam = [6, 7, 8]
        aut = [9, 10, 11]
        if win.count(m) == 1:
            print('Зима')
        else:
            if sprig.count(m) == 1:
                print('Весна')
            else:
                if sam.count(m) == 1:
                    print('Лето')
                else:
                    if aut.count(m) == 1:
                        print('Осень')
                    else:
                        print('Прошу вас от 1 до 12')
