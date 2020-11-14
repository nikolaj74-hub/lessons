def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    if b < a and b < c:
        return a + c
    else:
        return a + b


print(my_func(a=int(input()), b=int(input()), c=int(input())))
