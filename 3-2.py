#Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_info (name, surname, year, city, mail, phone):
    print(f'{surname} {name} {year} года рождения, проживает в городе {city}. Контактная информация: {mail}, {phone}.')

name_user = input('Введите имя\n')
surname_user = input('Введите фамилию\n')
year_user = input('Введите год рождения\n')
city_user = input('Введите город проживания\n')
mail_user = input('Ведите адрес электронной почты\n')
phone_user = input('Введите номер телефона\n')

user_info(surname=surname_user, name=name_user, phone=phone_user, city=city_user, year=year_user, mail=mail_user)