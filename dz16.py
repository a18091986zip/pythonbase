#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


#проверка числа на принадлежность к множеству рациональных, неотрицательных

firstday_distance = input('Сколько километров спортсмен пробежал в первый день? ')

while True:
    try:
        firstday_distance = float(firstday_distance)
        if firstday_distance < 0:
            firstday_distance = input(
                'Ну он же спортсмен! Он должен был пробежать хоть какое-то ПОЛОЖИТЕЛЬНОЕ РАЦИОНАЛЬНОЕ число километров. Попробуем ещё раз:\n')
            continue
        elif firstday_distance == 0:
            firstday_distance = input(
                'Я думаю, что спортсмен бежал, а не стоял на месте. Введите ПОЛОЖИТЕЛЬНОЕ РАЦИОНАЛЬНОЕ число километров:\n')
        else:
            break
    except ValueError:
        firstday_distance = input(
            'Давайте дистанция будет ПОЛОЖИТЕЛЬНЫМ РАЦИОНАЛЬНЫМ числом, ок?\nПопробуем ещё раз:\n')

summ_distance = input('Выясним, когда спортсмен пробежит заданное число километров. Введите это число:\n')

while True:
    try:
        summ_distance = float(summ_distance)
        if summ_distance < 0:
            summ_distance = input(
            'Ну он же спортсмен! Он должен был пробежать хоть какое-то ПОЛОЖИТЕЛЬНОЕ РАЦИОНАЛЬНОЕ число километров. Попробуем ещё раз:\n')
            continue
        elif summ_distance == 0:
            summ_distance = input(
                'Бегал-бегал и ничего не набегал? Попробуем ещё раз! Введите ПОЛОЖИТЕЛЬНОЕ РАЦИОНАЛЬНОЕ число>:\n')
        else:
            break
    except ValueError:
        summ_distance = input(
            'Давайте дистанция будет ПОЛОЖИТЕЛЬНЫМ РАЦИОНАЛЬНЫМ числом, ок?\nПопробуем ещё раз:\n')

i=1

distance = firstday_distance

while distance <= summ_distance:
    print(f'{i}-й день: {round(distance,2)}')
    i += 1
    distance *= 1.1

print(f'{i}-й день: {round(distance,2)}')
print(f'на {i}-й день спортсмен достиг результата - не менее {round(summ_distance,2)} км')


