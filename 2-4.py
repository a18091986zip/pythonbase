#Пользователь вводит строку из нескольких слов, разделенных пробелами. Вывести каждое слово с новой
#строки. Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.


my_string = input('Введите строку:\n')
i = 0
my_string_list = my_string.split()
for i in range (len(my_string_list)):
    if len(my_string_list[i]) > 10:
        print(f'{i+1}. {str(my_string_list[i])[:10]}')
    else:
        print(f'{i+1}. {my_string_list[i]}')
