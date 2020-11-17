from functools import reduce

print(reduce(lambda a, b: int(a) * int(b), range(100, 1000 + 1, 2)))
