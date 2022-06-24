# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Осуществить вывод данных о пользователе одной строкой

def application(**kwargs):
    return ' '.join(kwargs.values())


print(application(name=input('Введите имя: '), surname=input('Введите фамилию: '),
                  birth_year=input('Введите год рождения: '),
                  city=input('Введите город проживания: '),
                  phone_n=input('Ввведите контактный телефон: '),
                  e_mail=input('Введите адрес электронной почты: ')))
