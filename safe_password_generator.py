#  Генератор безопасных паролей.
# Описание проекта: программа генерирует заданное количество паролей
# и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for;
# Написание пользовательских функций;
# Работа с модулем random для генерации случайных чисел.

import random
import string
import time

def safe_password_generator(help):

    while help.lower() == 'n':
        time.sleep(0.7)
        print()
        print(
            'Ok. It`s fine that you decided to create the password yourself. \nIf you change your mind, this program '
            'will always help you.')
        break

    chars = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    chars = list(chars)
    random.shuffle(chars)

    if help.lower() == 'y':
        password = ''
        print()
        print(
            'Attention! This password will be generated from characters, that you can type on any computer keyboard.')
        time.sleep(6.0)
        print()
        len_password = int(input('Please, enter the length of your password: '))
        print()
        print('Please wait...')
        time.sleep(1.5)
        print()

        for char in range(len_password):
            password += random.choice(chars)

        print(password, '  - please. This unique password was created for you.', )


password = input('I can help you create a secure password. (yes = y, no = n): ')
safe_password_generator(password)
