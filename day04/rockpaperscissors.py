import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))

if choice >= 0 and choice <= 2:
    com_choice_idx = random.randint(0,2)

    computer_choice = choices[com_choice_idx]
    your_choice = choices[choice]

    print("You:\n")
    print(your_choice)

    print("Computer:\n")
    print(computer_choice)

    if choice == 0:
        if com_choice_idx == 0:
            print("Rock vs Rock: Draw!")
        elif com_choice_idx == 1:
            print("Rock vs Paper: You lose! Computer win!")
        else:
            print("Rock vs Scissors: You win!")
    elif choice == 1:
        if com_choice_idx == 0:
            print("Paper vs Rock: You win!")
        elif com_choice_idx == 1:
            print("Paper vs Paper: Draw!")
        else:
            print("Paper vs Scissors: You lose! Computer win!")
    else:
        if com_choice_idx == 0:
            print("Scissors vs Rock: You lose! Computer win")
        elif com_choice_idx == 1:
            print("Scissors vs Paper: You win!")
        else:
            print("Scissors vs Scissors: Draw!")
else:
    print("Invalid Input! Only Input 0, 1, 2")


