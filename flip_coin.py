# Авторская функция вывода случайных значений,
# получаемых при подбрасывании монетки.
# В качестве начальных значений случайного числа
# используется системное время из внутреннего генератора тактовых импульсов
# компьютера пользователя.

import random


def flip_coin(choice):
    while choice.lower() == 'y':
        print('Coin is flying ...')
        print('Heads' if random.randint(0, 1) == 0 else 'Tails')
        choice = input('Flip the coin again? (Yes = y, not = n): ')


decision = input('Flip the coin? (Yes = y, not = n): ')

print(flip_coin(decision))
