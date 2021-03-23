"""Создайте  собственный  класс-исключение,  обрабатывающий  ситуацию  деления  на  ноль.
Проверьте  его  работу  на  данных,  вводимых  пользователем.  При  вводе  нуля  в  качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, string):
        self.string = string

    @staticmethod
    def number_validation(string):
        a = False
        while a == False:
            try:
                string = float(string)
                a = True
            except:
                string = input("Вы ввели не число, повторите ввод:")
        return string

    @staticmethod
    def number_not_zero(number):
        while number == 0:
            number = MyException.number_validation(input('На ноль делить нельзя, повторим:'))
        return number


print(f'Результат: {MyException.number_validation(input("Введите числитель:")) / MyException.number_not_zero(MyException.number_validation(input("Введите знаменатель:")))}')




