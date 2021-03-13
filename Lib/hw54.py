#создать непрограммно текстовый файл со следующим содержимым: one - 1, two - 2, three - 3, four - 4.
#Напишите программу, открывающую файл на чтение и считываюшие построчно данные. При этом английские числительные
#должны заменяться на русские. Новый блок строк должен записыватья в новый текстовый файл

translate = {
    'One':'Один',
    'Two':'Два',
    'Three':'Три',
    'Four':'Четыре'
}
with open('hw41.txt', 'w') as new_f:
    pass
with open('hw4.txt', 'r') as f:
    for string in f:
        string_no_enter = string.replace('\n', '')
        string_no_space = string_no_enter.replace('  ', ' ')
        while '  ' in string_no_space:
             string_no_space = (string_no_space.replace('  ', ' ')).replace('\n','')
        if string_no_space.split(' ')[0] in translate.keys():
            with open('hw41.txt', 'a') as new_f:
                new_f.write(f'{translate.get(string_no_space.split(" ")[0])} - {string_no_space.split(" ")[2]} \n')



       

