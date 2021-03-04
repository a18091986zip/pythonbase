# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
from my_functions import check_not_string

stop=''
a = 0

def summ_number():
    str_user = input('Введите числа через пробел. Нажмите Enter по окончании ввода. Если Вы хотите завершить программу, напечатайте "!" \n')
    a = 0
#    for i in range(len(str_user)):
#        str_user_new += check_not_string(str_user[i])
    for el in str_user.split(' '):
        if el == '!':
            break
        else:
            el = check_not_string(el)
            a += float(el)
    return a,el



while stop != '!':
     return_summ_number = summ_number()
     a += return_summ_number[0]
     print(f'Сумма чисел: {a}')
     stop = return_summ_number[1]

