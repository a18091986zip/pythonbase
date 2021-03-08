#
def da_net(a):
    while True:
        if (a == 'да')|(a == 'нет'):
            break
        else:
            a = input('можно ввести только "да" или "нет"! Повторим: \n')
            continue
    return a



def lat_symb_or_znak (text):
    if text == '!':
        return '!'
    if text == '':
        return 'repeat'
    for letter in text:
        if not letter in "abcdefghjklmnopqrstuvwxyz":
            return 'repeat'
    return text

def BigFirst(text):
#   print(f'\n\033[32mВаша строка с прописной первой буквой:\033[33m {text.capitalize()}')
    return text.capitalize()


def check_not_string_not_null(a):
    while True:
        try:
            a = float(a)
            if a == 0:
                a = input('Не должно быть равно 0. Введите ещё раз:\n')
                continue
            else:
                break
        except ValueError:
            a = input('Нам требуется число, а не строка. Введите ещё раз:\n')
            continue
    return a

def check_not_string(a):
    while True:
        try:
            a = float(a)
            break
        except ValueError:
            a = input('Нам требуется число, а не строка. Введите ещё раз:\n')
            continue
    return a

def check_positive_int(a):
    while True:
        try:
            a = int(a)
            if a <= 0:
                a = input('Число должно быть положительным. Введите ещё раз:\n')
                continue
            else:
                break
        except ValueError:
            a = input('Нам требуется ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ число. Введите ещё раз:\n')
            continue
    return a

def check_positive_float(a):
    while True:
        try:
            a = float(a)
            if a <= 0:
                a = input('Число должно быть положительным. Введите ещё раз:\n')
                continue
            else:
                break
        except ValueError:
            a = input('Нам требуется положительное ЧИСЛО, а не строка. Введите ещё раз:\n')
            continue
    return a

def check_negative_int(a):
    while True:
        try:
            a = int(a)
            if a >= 0:
                a = input('Число должно быть ОТРИЦАТЕЛЬНЫМ. Введите ещё раз:\n')
                continue
            else:
                break
        except ValueError:
            a = input('Нам требуется отрицательное ЦЕЛОЕ ЧИСЛО. Введите ещё раз:\n')
            continue
    return a

