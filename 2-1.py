#создать список и заполнить его элементами различных типов данныхю Реализвать скрипт
#проверки типа данных каждого элемента. Использовать функцию type() для проверки типа
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе

from random import choice, randint

list = []
list_new_int = []
list_new_str = []
list_itog = []
step = 1

for i in range(5):
    l = input(f'Введите {i+1}-й элемент списка (числа или символы)')
    list.append(l)

for i in range(len(list)):
    try:
        list_new_int.append(int(list[i]))
    except ValueError:
        list_new_str.append(str(list[i]))

input("Формирую новый список из: \n"
      "- числовых элементов (целых, с плавающей точкой и комплексных) \n"
      "- байтовых элементов\n"
      "- логических элементов\n"
      "- строчных элементов\n"
      "- элементов в виде вложенного списка\n"
      "    НАЖМИТЕ 'Enter'")

if len(list_new_int) == 0:
    list_new_int.append(randint(0, 100))

while step < 3:
    list_itog.append(complex(choice(list_new_int), choice(list_new_int)))
    list_itog.append(int(choice(list_new_int)))
    list_itog.append(float(choice(list_new_int)))
    list_itog.append(bool(choice(list_new_str)))
    list_itog.append(bytes(choice(list_new_int)))
    list_itog.append(list_new_str)
    step+=1

for i in range (len(list_itog)):
    print(f'{i+1}-й элемент итогового списка: {list_itog[i]}\n'
          f'его тип: {type(list_itog[i])}')






