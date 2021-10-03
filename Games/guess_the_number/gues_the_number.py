from art import logo
import random


def chosen_number():
    the_number = random.randint(1, 101)
    return the_number


secreat_number = chosen_number()


def set_difficulty():
    level = int(input("Choose the difficulty [1] for 'hard' [2] for 'easy':\t"))
    if level == 1:
        attemps = 5
    else:
        attemps = 10
    return attemps


def check_answer(guess_num, secreat_number, attemps):
    if guess_num == secreat_number:
        return True
    else:
        if attemps <= 1:
            return False
        elif guess_num > secreat_number:
            return "Too high\n"
        elif guess_num < secreat_number:
            return "Too low\n"


def game():
    secreat_number = chosen_number()
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 to 100")
    print(f"Pssst, the secreat number is {secreat_number}\n")

    attemps = set_difficulty()

    is_game_over = False
    while not is_game_over:
        print(f"You have {attemps} attemps remaining to guess the number")
        guess_num = int(input("Guess a number (1 ~ 100):\t"))
        answer = check_answer(guess_num, secreat_number, attemps)
        if answer == True:
            print(f"You win. {secreat_number} was the secreat number")
            is_game_over = True
        elif answer == False:
            print(" === GAME OVER === ")
            print(f"The secreat number was {secreat_number}")
            is_game_over = True
        else:
            print(answer)

        attemps -= 1


game()