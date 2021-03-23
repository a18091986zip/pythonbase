"""Реализовать  класс  «Дата»,  функция-конструктор  которого  должна  принимать  дату  в  виде
строки  формата  «день-месяц-год».  В  рамках  класса  реализовать  два  метода.  Первый,  с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных."""


class Data:
    str_array = []
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_str_to_date_number(cls, date_str):
        str_array = date_str.split('-')
        try:
            day = int(str_array[0])
            month = int(str_array[1])
            year = int(str_array[2])
        except:
            print('что-то пошло не так')
            return False
        return day, month, year

    @staticmethod
    def validation(date_str):
        print('*************************************')
        if 1<=Data.date_str_to_date_number(date_str)[0]<=31:
            print('Валидация дня прошла успешно')
        else:
            print('Число ДНЯ вне диапазона 1-31')
        if 1<=Data.date_str_to_date_number(date_str)[1]<=12:
            print('Валидация месяца прошла успешно')
        else:
            print('Число МЕСЯЦА вне диапазона 1-31')
        if 0<=Data.date_str_to_date_number(date_str)[2]<=2021:
            print('Валидация года прошла успешно')
        else:
            print('или речь о БУДУЩЕМ или ГОД введен неверно')

a = False
while a == False:
    string = input('Введите дату в формате "dd-mm-yyyy": ')
    a = Data.date_str_to_date_number(string)
print(f'Дата: {Data.date_str_to_date_number(string)[0]} день {Data.date_str_to_date_number(string)[1]} месяца {Data.date_str_to_date_number(string)[2]} года')
Data.validation(string)
