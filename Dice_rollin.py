import random
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('Rolled dice are {} and {}'.format(dice1,dice2))
dice_roll()