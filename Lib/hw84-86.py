"""4. Начните  работу  над  проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные  типы  оргтехники  (принтер,  сканер,  ксерокс).  В  базовом  классе  определите
параметры,  общие  для  приведённых  типов.  В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники  на  склад  и  передачу  в  определённое  подразделение  компании.  Для  хранения
данных  о  наименовании  и  количестве  единиц  оргтехники,  а  также  других  данных,  можно
использовать любую подходящую структуру (например, словарь).
6. Продолжить  работу  над  вторым  заданием.  Реализуйте  механизм  валидации  вводимых
пользователем  данных.  Например,  для  указания  количества  принтеров,  отправленных  на
склад, нельзя использовать строковый тип данных. """
from abc import ABC, abstractmethod
from prettytable import PrettyTable
was = PrettyTable()
now = PrettyTable()

class Warehouse(ABC):
    """ Этот класс сам ничего не делает, только обязывает дочерние классы реализовывать определенные методы """
    @abstractmethod
    def count_give_from_warehouse(self):
        pass

    def count_give_to_warehouse(self):
        pass

class Office_Equipment(Warehouse):
    """ Этот класс определяет общие параметры для экземпляров классов-наследников и статические методы"""
    def __init__(self,name, count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue):
        self.name = name
        self.count_in_warehouse = count_in_warehouse
        self.count_in_service = count_in_service
        self.count_in_office = count_in_office
        self.brand = brand
        self.year_of_issue = year_of_issue

    @staticmethod
    def count_give_from_warehouse(self, count_give):
        a = False
        while a == False:
            try:
                count_give = int(count_give)
                a = True
            except:
                count_give = input('количество должно быть целым положительным числом, повторите:')
        self.count_give = count_give
        self.count_in_warehouse -= self.count_give
        return self.count_in_warehouse
    @staticmethod
    def count_give_to_warehouse(self, count_give):
        a = False
        while a == False:
            try:
                count_give = int(count_give)
                a = True
            except:
                count_give = input('количество должно быть целым положительным числом, повторите:')
        self.count_give = count_give
        self.count_in_warehouse += self.count_give
        return self.count_in_warehouse

    def count_give_in_office(self, count_give):
        self.count_give_from_warehouse(self, count_give)
        self.count_in_office += self.count_give
        return self.count_in_office

    def count_give_from_office(self, count_give):
        self.count_give_to_warehouse(self, count_give)
        self.count_in_office -= self.count_give
        return self.count_in_office

    def count_give_in_service(self, count_give):
        self.count_give_from_warehouse(self, count_give)
        self.count_in_service += self.count_give
        return self.count_in_service

    def count_give_from_service(self, count_give):
        self.count_give_to_warehouse(self, count_give)
        self.count_in_service -= self.count_give
        return self.count_in_service
    def where_equipment(self):
        return self.count_in_office, self.count_in_service, self.count_in_warehouse



class PC(Office_Equipment):

    def __init__(self,name,count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue, type):
        super().__init__(name,count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue)
        self.type = type

class Printer(Office_Equipment):

    def __init__(self,name,count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue, model):
        super().__init__(name,count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue)
        self.model = model

class Shredder(Office_Equipment):

    def __init__(self,name, count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue, clas):
        super().__init__(name, count_in_warehouse, count_in_service, count_in_office, brand, year_of_issue)
        self.clas = clas

print(f'Class Warehouse: \n {Warehouse.__doc__}\n*******************************************************************************************************\n'
      f'Class Office_Equipmetn: \n {Office_Equipment.__doc__}\n*******************************************************************************************************')
print(f'Классы-наследники: PC, Printer, Shredder. Наследуют общие аттрибуты, \n опредеденные в классе Office_Equipment'
      f' и вводят индивидуальные:\n'
      f'- type для PC (например монолок, офисный, сервер)\n'
      f'- model - модель принтера\n'
      f'- clas - класс производительности шредера\n'
      f'*****************************************************************************************************')
was.field_names = ['Наименование', 'Производитель', 'На складе', 'В офисе', 'В сервисе']

comp1 = PC('ПК',12,3,2,'asus',2010,'моноблок')
comp2 = PC('ПК',24,48,10,'hp',2010,'сервер')
printer = Printer('принтер',35,3,10, 'hp', 2020, 'M554dn')
shredder = Shredder('шреддер',2,1,1, 'Brauberg', 2018, 'третий')

for i in [comp1,comp2,printer,shredder]:
    was.add_row([i.name, i.brand, i.count_in_warehouse, i.count_in_office, i.count_in_service])
print(f'Текущее состояние:\n{was}')
print(f'Давайте переместим несколько единиц техники')
comp1.count_give_in_office(input(f'сколько компьютеров 1 типа отправим со склада в офис?'))
comp1.count_give_in_service(input(f'сколько компьютеров 1 типа отправим со склада в сервис?'))
printer.count_give_from_office(input(f'сколько принтеров заберем из офиса на склад?'))
printer.count_give_from_service(input(f'сколько принтеров вернем из сервиса на склад?'))

now.field_names = ['Наименование', 'Производитель', 'На складе', 'В офисе', 'В сервисе']

for i in [comp1,comp2,printer,shredder]:
    now.add_row([i.name, i.brand, i.count_in_warehouse, i.count_in_office, i.count_in_service])

print(f'После произведенных действий:\n{now}')




