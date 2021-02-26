#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число: ')

#проверка числа на принадлежность к множеству целых, положительных

while True:
    try:
        number = int(number)
        if number < 0:
            number = input('Давайте это будет ПОЛОЖИТЕЛЬНЫМ ЦЕЛЫМ числом, ок?\nПопробуем ещё раз:\n')
            continue
        else:
            break
    except ValueError:
        number = input('Давайте это будет ЧИСЛОМ и число будет ЦЕЛЫМ, ок?\nПопробуем ещё раз:\n')

# whole_part - челая часть от деления
# remain_part - остаток от деления

whole_part = number
remain_part_max = -1

while whole_part > 1:
    remain_part = whole_part % 10
    if remain_part_max < remain_part:
        remain_part_max = remain_part
    whole_part = whole_part // 10

print(f'Максимальная цифра Вашего числа: {remain_part_max}')


