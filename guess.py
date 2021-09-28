# Угадайка чисел.
# Описание проекта: программа генерирует случайное число
# в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число,
# то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
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


def guessing(your_choice):
    event = random.randint(1, 20)

    number_of_attempted = 0
    while guess == 'n':
        time.sleep(0.7)
        print('Ok. Have a nice day and goodbye.')
        break

    while guess == 'y':
        time.sleep(0.5)
        your_choice = input('Guess the number from 1 to 20: ')
        if 1 <= int(your_choice) <= 20:
            if int(your_choice) == event:
                number_of_attempted += 1
                time.sleep(1.0)
                print()
                print('You got it, congratulations!')
                print()
                time.sleep(1.5)
                print('You guessed from the', number_of_attempted,
                      'attempt. Thank you for playing. See you soon...')
                break
            elif int(your_choice) > event:
                number_of_attempted += 1
                time.sleep(0.5)
                print('Too much, try again.')
                continue
            else:
                number_of_attempted += 1
                time.sleep(0.5)
                print('Too small, try again.')
                continue
        else:
            time.sleep(1.1)
            print('You did not enter a number from the specified range.')
            continue


guess = input('Welcome to the game. Do you want to play guessing? (yes = y, not = n): ')
guessing(guess)
