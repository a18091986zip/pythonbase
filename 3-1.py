#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


from my_functions import check_not_string_not_null, check_not_string

#подключаемые функции - для проверки вводимых данных - не строка, не ноль

def division (a,b):
    return round(a / b,3)

delimoe = check_not_string(input(f'введите делимое:\n'))
delitel = check_not_string_not_null(input(f'введите делитель\n'))
print(division(delimoe,delitel))
