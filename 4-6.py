#Реализовать два небольших скрипта:
#● итератор, генерирующий целые числа, начиная с указанного;
#● итератор, повторяющий элементы некоторого списка, определённого заранее.
#Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
#создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
#завершаем  цикл.  Вторым  пунктом  необходимо  предусмотреть  условие,  при  котором
#повторение элементов списка прекратится..

from itertools import count, cycle
from my_functions import da_net
list = []
a = ''
b = ''
d = {}

print('Сейчас сформируем словарь, ключи которого будут генерироваться с помощью count(), \nа значения - '
      'с помощью cycle() из элементов вводимого пользователем списка.')

for number in count(1):
    if a == 'нет':
        break
    else:
        for symb in cycle(input(f'Введите список для формирования значений ключа {number}\n').split(' ')):
            if b == 'нет':
                break
            else:
                 list +=[symb]
                 print(number,list)
                 b = input(f'Желаете добавить элементов из списка?\n'
                           f'Напечатайте "да" или "нет"\n')
                 da_net(b)
        d [number] = list
        list = []
        print('Текущий словарь:')
        print("\n".join(f'{k}:{v}' for k,v in d.items()))
        a = input(f'Желаете добавить строку?\n'
              'Напечатайте "да" или "нет"\n')
        da_net(a)
        b = ''
