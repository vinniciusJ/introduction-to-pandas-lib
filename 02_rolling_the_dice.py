from random import randint

rolled_dices = [randint(1, 6) for i in range(100)]

for i in range(1, 7):
    print(f'O número {i} apareceu {rolled_dices.count(i)} vezes')