# Rock-Scissors-Paper Game
import random
play = int(input('How many times do you want to play: '))
player = input(f'Choose R or S or P (not case sensitive): ')
comp = random.choice(['r','s','p'])
won = (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r')
start = 0

# if won:
#     print('You won')
# elif not won:
#     won = False
#     if player == comp:
#         print('A tie')
#     else:
#         print('You lost')
# print(comp)
if won:
    print('You won')
while not won:
    won = False
    if start < play:
        input('Come again: ')
        if player == comp:
            print('A tie')
            start += 1
    else:
        print('You lost')
        break
