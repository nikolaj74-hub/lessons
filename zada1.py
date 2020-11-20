f = open("first.txt", "w")
while True:
    s = input('введите строку:')
    if s == '': break  # проверка на пустую строку
    f.write(s + '\n')
f.close()
f = open("first.txt", "r")
content = f.read()
print(content)
f.close()
