# 7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
#z1+z2=(a+b*i)+(c+d*i)=(a+c)+(b+d)*i
# результата.
class Complex_number:
    def __init__(self,a,b,c,d):
        self.a=complex(a,b)
        self.b=complex(c,d)


    def add_complex(self):
        return self.a+self.b

    def mult_complex(self):
        return self.a*self.b

a=Complex_number(6,2,4,5)
print(a.add_complex())
print(a.mult_complex())