

from functools import reduce

print(reduce(lambda a, b: int(a) * int(b), range(1, 1+int(input('введите номер эл')))))

###############################################################################################
from math import factorial

def fact():
    for el in {factorial(int(input('введите номер элемента')))}:
        yield el

f = fact()

print(f)
for el in f:
    print(el)
