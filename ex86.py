# Create a program that helps a MEGASENA player generate bets.
# The program will ask how many games to generate
# and will draw 6 numbers between 1 and 60 for each game, storing
# everything in a composite list.
import time
games = list()
bets = list()
from random import randint
print('='*40)
print(f'{"MEGA SENA GAME":^40}')
print('='*40)
n = int(input('How many games will be generated: '))
for _ in range(0, n):
    for _ in range(0, 6):
        num = randint(1, 60)
        if num not in games:
            games.append(num)
        else:
            while num in games:
                num = randint(1, 60)
            games.append(num)
    bets.append(games[:])
    games.clear()
for c in range(0, len(bets)):
    print(f'Your {c} numbers are: {bets[c]}')
    time.sleep(1)
