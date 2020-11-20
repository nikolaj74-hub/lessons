#      Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
#      подсчет количества строк, количеста слов в каждой строке.
lines = [line.strip() for line in open('zadanie2.txt')]
print(lines)
print(len(lines))

s = 0
while s < len(lines) - 1:
    a = len(lines[s])
    print(a)

    s = s + 1
