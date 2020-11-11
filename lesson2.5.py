lis = [1, 9, 7, 4, 2, 2]
print(lis)
a = int(input('Введите новый элемент рейтинга:'))
s = lis.count(a)  # пер s присв.зн.=колич.элементов равных пер а
lis.append(a)  # в конец списка добавляем знач.пер. а
t = lis.index(a)  # пер  t присв номер индекса первого элемента равному а
# sum = lis.index(a) + lis.count(a)# пер. sum пр.зн. суммы
su = t + s  # sum = lis.index(a) + lis.count(a)
lis.insert(su, (a))  # размещаем на позиции индекса с зн. sum элемент с зн. а
lis.sort(reverse=True)  # сортируем по убыванию
lis.remove(a)  # удоляем из списка первый элемент с зн. а
print(lis)
