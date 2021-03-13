#создать программно текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#программа должна подсчитывать сумму чисел в файле и выводить её на экран

from my_functions import check_not_string

summ = 0
with open('hw5.txt', 'w') as new_f:
    pass
with open('hw5.txt', 'a') as new_f:
    while True:
        a = input(f'Введите новое число в файл. Для завершения - введите пустую строку.')
        if a == '':
            break
        else:
            new_f.write(f'{a} ')
with open('hw5.txt', 'r') as new_f:
    for string in new_f:
        string_no_space = string.split(' ')
        for el in string_no_space:
            if check_not_string(el)==True:
                summ += float(el)
print(f'Сумма записанных в файл чисел равна: {summ}')
