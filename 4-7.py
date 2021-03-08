# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом:
# for el in fact(n). Она отвечает за получение факториала числа..
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from my_functions import check_positive_int

def fact(n):
    a=1
    for i in range(1, n+1):
        a *= i
        yield i,a

n = check_positive_int(input(f'Сейчас будут выведены факториалы чисел от 1 до N, введите N:\n'))

for i,el in fact(n):
   print(f'{i}! = {el}')
