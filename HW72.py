"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.


"""

from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def coat(self):
        pass
    @abstractmethod
    def costume(self):
        pass

class Textile(Clothes):
    def __init__(self, name):
        super().__init__(name)

    @property
    def cloth_name(self):
        return self.name

    def coat(self, v):
        if self.name == 'coat':
            self.v = v
            textile = v / 6.5 + 0.5
            return f'На {self.cloth_name} потребуется {textile}'
        else:
           pass

    def costume(self, h):
        if self.name == 'costume':
            self.h = h
            textile = 2*h + 0.3
            return f'На {self.cloth_name} потребуется {textile}'
        else:
            pass

cloth1 = Textile('costume')
print(cloth1.costume(1))
cloth2 = Textile('coat')
print(cloth2.coat(13))



