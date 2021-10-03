from random import randint

choice = int(input("What do you choose?\n Type 0 for rock , 1 for paper, 2 Scissors: "))

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

options = [rock, paper, scissors]
computer_choice = options[randint(0,2)]

if (choice == 0):
  choice = options[0]
elif (choice == 1):
  choice = options[1]
else:
  choice = options[2]


if (choice == computer_choice):
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("D R A W")

elif (choice == 0 and computer_choice == 2):
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("You win !!!")

elif(choice == 2 and computer_choice == 0):
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("You loose")

elif(choice == 1 and computer_choice == 0):
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("You win !!!")

elif(choice == 0 and computer_choice == 1):
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("You loose")

elif(choice == 2 and computer_choice == 1):
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("You win")
else:
  print(f"you\n{choice}\nx\n\ncomputer\n{computer_choice}")
  print("You loose")




