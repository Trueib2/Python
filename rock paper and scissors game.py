choices= ['rock', 'paper','scissors']
players_choice = input('Choose your weapon (rock, paper, or scissors): ').lower()
print('\nYou Chose: ', players_choice)

import random
computer_choice = random.choice(choices)

print('Computer chose', computer_choice)
if computer_choice == players_choice:
    print("It's a tie")
elif (players_choice == 'rock' and computer_choice == 'scissors' or
      players_choice == 'scissors' and computer_choice == 'paper'or
      players_choice == 'paper' and computer_choice == 'rock' ) :
    print('You win')

else :
    print('Computer won')
