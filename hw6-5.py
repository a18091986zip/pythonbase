# Реализовать класс Stationery (канцелярская принадлежность)
# - определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение "запуск отрисовки"
# - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер)
# - в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Это ручка')
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Это карандаш')
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Это маркер')

pen = Stationery('ручка')
pen.draw()
pen = Pen ('ручка')
pen.draw()
print('\n-----------------------------\n')
pencil = Stationery('карандаш')
pencil.draw()
pencil = Pencil('карандаш')
pencil.draw()
print('\n-----------------------------\n')
handle = Stationery('маркер')
handle.draw()
handle = Handle('маркер')
handle.draw()