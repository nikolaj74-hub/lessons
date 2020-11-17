from itertools import cycle
from sys import argv
name, a, b = argv
b = int(b)
print(' список:', a)
print('сколько раз повторить?', b)

c = 0
for h in cycle(a):
    if c >= b:
        break
    print(h)
    c += 1