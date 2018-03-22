import random

foo = ["Rock", "Paper", "Scissors"]
comp_choice = random.choice(foo)

human_choice = input('Choose Paper, Rock or Scissors:\n')

if human_choice == 'Rock' and comp_choice == "Scissors":
    print("WINNER WINNER CHICKEN DINNER!")
elif human_choice == 'Paper' and comp_choice == 'Rock':
    print('WINNER WINNER CHICKEN DINNER!')
elif human_choice == 'Scissors' and comp_choice == 'Paper':
    print('WINNER WINNER CHICKEN DINNER!')
elif human_choice == comp_choice:
    print('Tie!')
else:
    print("You Lose!")
print(comp_choice)