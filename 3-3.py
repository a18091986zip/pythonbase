#Реализовать функцию my_func(), # которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
from my_functions import check_not_string

def summ_two_max (a,b,c):
    list = [a, b, c]
    list.pop(list.index(min(list)))
    return sum(list)

def info_input (i):
    a = input(f'Введите {i} число\n')
    a = check_not_string(a)
    return a

a=info_input(1)
b=info_input(2)
c=info_input(3)

print(f'сумма двух наибольших элементов:\n{summ_two_max(a,b,c)}')