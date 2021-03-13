# создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20000, вывести фамилии этих сотрудников.
# Выпонить подсчет средней величины дохода сотрудников.


with open('hw3.txt', 'r') as new_f:
    summ = 0
    i = 0
    surname = ''
    for string in new_f:
        string_no_enter = string.replace('\n', '')
        string_no_space = string_no_enter.replace('  ', ' ')
        while '  ' in string_no_space:
            string_no_space = (string_no_space.replace('  ', ' ')).replace('\n', '')
        if float(string_no_space.split(' ')[1]) < 20000:
            surname = string_no_space.split(' ')[1]
            print(f'Оклад {string_no_space.split(" ")[0]}(-а) < 20000')
        summ += float(string_no_space.split(' ')[1])
        i += 1
    print(f'Средняя величина доходов сотрудников составляет: {round(summ / i, 2)}')




