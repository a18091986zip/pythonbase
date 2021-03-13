#создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
#строк и слов в каждой строке.

with open('hw2.txt', 'r') as new_f:
    i = 1
    for string in new_f:
        j = 0
        string_no_space = string.replace('  ', ' ')
        while '  ' in string_no_space:
            string_no_space = string_no_space.replace('  ', ' ')
        for word in string_no_space.split(' '):
            j += 1
        print(f'В {i}-й строке {j} слов(а)')
        i += 1



