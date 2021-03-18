# Реализовать базовый класс Car
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# - добавьте в базовый класс метод Show_speed, который должен показывать текущую скорость автомобиля
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')
    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def towncar_method(self):
        print('ПАРКЕТНИК')
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости')
        else:
            print('Вы едете в рамках установленных скоростных ограничений')
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def sportcar_method(self):
        print('СПОРТИВНАЯ')
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def workcar_method(self):
        print('СЛУЖЕБНАЯ')
    def show_speed(self):
        if self.speed>60:
            print(f'Превышение скорости')
        else:
            print('Вы едете в рамках установленных скоростных ограничений')
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def policecar_method(self):
        if self.is_police == True:
            print('ПОЛИЦЕЙСКАЯ')


print('\n-----------------------------\n')
ford = PoliceCar(200,'синий','ford', True)
ford.policecar_method()
print(f'Это {ford.name}. Её цвет {ford.color}. Это полицейская машина: {ford.is_police}')
ford.go()
ford.turn('юг')
ford.stop()
ford.show_speed()
print('\n-----------------------------\n')

volkswagen = TownCar(80,'желтый','volkswagen', False)
volkswagen.towncar_method()
print(f'Это {volkswagen.name}. Её цвет {volkswagen.color}. Это полицейская машина: {volkswagen.is_police}')
volkswagen.go()
volkswagen.turn('юг')
volkswagen.stop()
volkswagen.show_speed()
print('\n-----------------------------\n')
mersedes = WorkCar(20,'черный','mercedes', False)
mersedes.workcar_method()
print(f'Это {mersedes.name}. Её цвет {mersedes.color}. Это полицейская машина: {mersedes.is_police}')
mersedes.go()
mersedes.turn('юг')
mersedes.stop()
mersedes.show_speed()
print('\n-----------------------------\n')

ferrari = SportCar(300,'красный','ferrari', False)
ferrari.sportcar_method()
print(f'Это {ferrari.name}. Её цвет {ferrari.color}. Это полицейская машина: {ferrari.is_police}')
ferrari.go()
ferrari.turn('юг')
ferrari.stop()
ferrari.show_speed()
print('\n-----------------------------\n')