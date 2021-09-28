# Авторская функция вывода случайных значений,
# получаемых при бросании игральных кубиков.
# В качестве начальных значений случайного числа
# используется системное время из внутреннего генератора тактовых импульсов
# компьютера пользователя.

import random


def use_dice(plant_dice):
    while plant_dice.lower() == 'y':
        print('Roll the dice ... ')
        print('Dice face values:')
        print(random.randint(1, 6), random.randint(1, 6))
        plant_dice = input('Plant the dice again? (Yes = y, not = n): ')


decision = input('Plant the dice? (Yes = y, not = n): ')

print(use_dice(decision))
