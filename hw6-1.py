#Создать класс TrafficLight (светофор)
# - определить у него 1 атрибут color (цвет) и метод running (запуск)
# - атрибут реализовать как приватный
# - в рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый
# - продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) - 2 секунды, третьего
# (зеленый) на Ваше усмотрение
# - переключение между режимами должно происходить только в укзанном порядке (красный, желтый, зеленый)
# - проверить работу примера, создав экземпляр и вызвав описанный метод


import time
print('Сейчас Вы попробуете побыть регулировщиком движения, переключающим светофор.\n'
      'Помните, что у светофора три цвета: красный, желтый и зеленый и переключатся они должны последовательно')
class TraficLight:
    def running(self):
        self.__colour = input('Ведите цвет светофора: ')
        if ((self.__colour == 'красный') or (self.__colour =='зеленый')):
            print('Подождите, через 7 секунд цвет светофора нужно будет переключить')
            time.sleep(2)
            return self.__colour
        elif self.__colour == 'желтый':
            print('Подождите, через 2 секунды цвет светофора нужно будет переключить')
            time.sleep(2)
            return self.__colour
        else: print('нет такого цвета, все сломалось')


check = True
colour = TraficLight()
colour_new = colour.running()
if colour_new != None:
    colour_previous = colour_new
    colour_new = colour.running()
if ((colour_new == 'желтый' and colour_previous == 'красный') or
   (colour_new == 'желтый' and colour_previous == 'зеленый') or
   (colour_new == 'зеленый' and colour_previous == 'желтый') or
   (colour_new == 'красный' and colour_previous == 'желтый')):
    colour_previous_previous = colour_previous
    colour_previous = colour_new
    check = True
elif colour_new == None:
    check = False
else:
    print('Неправильный порядок следования цветов, пробка...')
    check = False

while (check == True):
    colour = TraficLight()
    colour_new = colour.running()
    if ((colour_previous == 'зеленый') or (colour_previous == 'красный')) and (colour_new == 'желтый'):
        colour_previous_previous = colour_previous
        colour_previous = colour_new
        check = True
    elif (colour_previous == 'желтый') and (colour_previous_previous =='красный') and (colour_new == 'зеленый'):
        colour_previous_previous = colour_previous
        colour_previous = colour_new
        check = True
    elif (colour_previous == 'желтый') and (colour_previous_previous == 'зеленый') and (colour_new == 'красный'):
        colour_previous_previous = colour_previous
        colour_previous = colour_new
        check = True
    elif colour_new == None:
        check = False
    else:
        print('Неправильный порядок следования цветов, пробка...')
        check = False


