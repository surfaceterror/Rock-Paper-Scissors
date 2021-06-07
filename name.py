# This is a game of rock, paper, scissors

from random import randint

print('Welcome to my python game: Rock, Paper, Scissors. Please enjoy!')

# Getting computers choice
computer = randint(1,3)

#Getting players choice
player = input('Options: \n 1. Rock \n 2. Paper \n 3. Scissors \n What is your choice: ')

# 1 == Rock
# 2 == Paper
# 3 == Scissors
#
# Rock beats Scissors
# Paper beats Rock
# Scissors beats paper
#

