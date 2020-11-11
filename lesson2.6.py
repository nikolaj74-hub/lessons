ch = int(input('Сколько  товаров ? :'))
m_list = []
a_list = []
b_list = []
c_list = []
i = 0
while i <= ch - 1:
    if i <= ch - 1:
        a = input('название-')
        b = input('цена-')
        c = input('количество-')
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
        n_dict = {'название': a_list}
        c_dict = {'цена': b_list}
        count_dict = {' количество': c_list}
        my_tup = tuple([i + 1, {'название': a, 'цена': b, 'количество': c}])
        m_list.append(my_tup)
        print()
        print('Товар', i + 2)
        print()
        i = i + 1
else:
    for n in m_list:
        print(n)
    print(n_dict)
    print(c_dict)
    print(count_dict)
