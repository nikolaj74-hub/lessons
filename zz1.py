# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.
class Data:
    def __init__(self, data):
        self.data = data
        print(self.data)

    @classmethod
    def learn(cls, data):
        s = [int(i) for i in data.split('-') if i.isdigit()]
        return s

    @staticmethod
    def validator(data):

        s = [int(i) for i in data.split('-') if i.isdigit()]

        if s[0] > 31 or s[0] < 1:
            print('в месяце нет столько дней')

        if s[1] > 12 or s[1] < 1:
            print('нет столько месяцев в году')

        if s[2] == 0:
            print('года с такими значениями нет')


a = Data('1-2-1900')
a.learn('1-2-3')
print(Data.learn('1-12-2018'))
Data.validator('34-89-000')
