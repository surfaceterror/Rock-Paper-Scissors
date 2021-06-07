# This is a game of rock, paper, scissors

from random import randint

print('Welcome to my python game: Rock, Paper, Scissors. Please enjoy!')

# 1 == Rock
# 2 == Paper
# 3 == Scissors
# Rock beats Scissors
# Paper beats Rock
# Scissors beats paper



#Getting players choice
player = input('Options: \n 1. Rock \n 2. Paper \n 3. Scissors \n What is your choice: ')
# Making player chioice into an int for if/then statement.
player = int(player)
if int(player) > 3:
    print('Invalid entry')

# Getting computers choice
computer = randint(1,3)

def game(computer, player):
    if (computer == 1) and (player == 2):
        print('Paper beats Rock! YOU WIN!!')
    elif (computer == 1) and (player == 3):
        print('Rock beats Scissors :( Better luck next time')
    elif (computer == 2) and (player == 1):
        print('Paper beats rock. Better luck next time!')
    elif (computer == 2) and (player == 3):
        print('Scissors beats paper! YOU WIN!!')
    elif (computer == 3) and (player == 1):
        print('Rock beats Scissors. YOU WIN!!')
    elif (computer == 3) and (player == 2):
        print('Scissors beats paper. Better luck next time!')
    else:
        print('TIE!')

game(computer, player)

