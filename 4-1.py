#Реализовать  скрипт,  в  котором  должна  быть  предусмотрена  функция  расчёта  заработной
#платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
#время  выполнения  расчёта  для  конкретных  значений  необходимо  запускать  скрипт  с
#параметрами.

from sys import argv
from my_functions import check_positive_float

script_name, hour, rate, premium = argv

print(f'Проверяем, что Вы ввели положительные числа')

hour, rate, premium = check_positive_float(hour),check_positive_float(rate),check_positive_float(premium)

print(f'Заработная плата сотрудника: {float(hour)*float(rate)+float(premium)}')

