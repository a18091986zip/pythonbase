"""Реализовать  проект  «Операции  с  комплексными  числами».  Создайте  класс  «Комплексное
число».  Реализуйте  перегрузку  методов  сложения  и  умножения  комплексных  чисел.
Проверьте  работу  проекта.  Для  этого  создаёте  экземпляры  класса  (комплексные  числа),
выполните  сложение  и  умножение  созданных  экземпляров.  Проверьте  корректность
полученного результата.


"""


class ComplexNumber:

    def __init__(self, number):
        self.number = number
        self.real = float(number[0])
        self.imaginary = float(number[1])

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        summ = [real, imaginary]
        print(f'Сумма: {ComplexNumber(summ)}')

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + other.real * self.imaginary
        mul = [real,imaginary]
        print(f'Произведение: {ComplexNumber(mul)}')

    def __str__(self):

        if self.imaginary < 0:
            return f'{self.real}{self.imaginary}i'
        elif self.imaginary == 0:
            return f'{self.real}'
        else:
            return f'{self.real}+{self.imaginary}i'


number_1 = [input(f'Введите действительную часть первого комплексного числа: '), input(f'Введите мнимую часть первого комплексного числа: ')]
number_2 = [input(f'Введите действительную часть второго комплексного числа: '), input(f'Введите мнимую часть второго комплексного числа: ')]
number_1 = ComplexNumber(number_1)
number_2 = ComplexNumber(number_2)
print('********************************')
print(f'Первое число: {number_1}')
print(f'Второе число: {number_2}')
print('********************************')
number_1+number_2
number_1*number_2


