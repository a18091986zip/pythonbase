#Реализовать базовый класс Worker (работник)
# - определить атрибуты: name, surname, position (должность), income (доход)
# - последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage":wage, "bonus":bonus}
# - создать класс Position (должность) на базе класса Worker
# - в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income)
# - проверить работу примера на реальных данных: создать экземляры класса Position,
# передать данные, проверить значения атрибутов, вызвать метод экземпляров

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 5, 'bonus': 10}

class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')
    def get_total_income(self):
        print(f"Полный доход: {self._income['wage'] + self._income['bonus']}")


employee1 = Position('Ivan', 'Ivanov', 'Программист')
print(employee1.name)
print(employee1.surname)
print(employee1.position)
employee1.get_full_name()
employee1.get_total_income()
