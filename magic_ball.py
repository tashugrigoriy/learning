# Магический шар 8
# Описание проекта: магический шар 8 (шар судьбы)
# — шуточный способ предсказывать будущее.
# Программа должна просить пользователя задать некий вопрос,
# чтобы случайным образом на него ответить.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.

import random
import time


def magic_ball(ask):
    answers = ['Undoubtedly', 'I think so, yes', 'It is not yet clear, try it again', 'Don`t you dare',
               'Foregone conclusion', 'Most likely', 'Ask later', 'The answer`s no', 'No doubt',
               'Good prospects', 'It is better not to tell', 'Not according to my data', 'definitely - yes',
               'Sings say yes', 'it`s impossible to predict', 'prospects not so good',
               'You can be sure', 'Yes', 'Concentrate and ask again', 'It`s very doubtful']

    while ask.lower() == 'n':
        time.sleep(0.7)
        print('Ok. The world without magic is also good. Have a nice day.')
        break

    while ask.lower() == 'y':
        time.sleep(0.5)
        name = input('What to call you?  ')
        print()
        time.sleep(0.5)

        ask = input(
            'Nice to meet you, ' + name + '. Please, you can ask the depths of magic about what`s bothering you...:  ')
        print()
        print(random.choice(answers))
        print()
        time.sleep(1.5)
        ask_2 = input('You can ask one more question... (Yes = y, no = n):  ')

        if ask_2.lower() == 'n':
            time.sleep(0.5)
            print('Ok, ' + name + ', see you soon...')
            break

        while ask_2.lower() == 'y':
            print()
            ask = input('Great ' + name + '. I hear you...:  ')
            print()
            print(random.choice(answers))
            print()
            time.sleep(1.5)
            ask_3 = input('You can ask one more question... (Yes = y, no = n):  ')
            if ask_3.lower() == 'n':
                time.sleep(0.5)
                print('Ok, ' + name + ', may be you`ll come again...')
                return


ask_me = input('Welcome to the world of magic. You want to ask question, right? (Yes = y, no = n): ')
magic_ball(ask_me)

