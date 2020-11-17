from itertools import count
from sys import argv
name, i, z = argv
i = int(i)
z = int(z)
print('с какого числа начнем:', i)
print('каким закончим:', z)
for el in count(i):
  if el > z:
    break
  else:
    print(el)
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
