import random
import math



comp_choice = "Rock", "Paper", "Scissors"
random.choice(comp_choice)

human_choice = input('Choose paper, rock or scissors:\n')

if human_choice == 'Rock' and comp_choice == "Scissors":
    print("You Win!")
elif human_choice == 'Paper' and comp_choice == 'Rock':
    print('You Win!')
elif human_choice == 'Scissors' and comp_choice == 'Paper':
    print('You win!')
else:
    print("You Lose!")
print(comp_choice)