from art import logo, vs
from game_data import data
from replit import clear
from random import randint


# função para gerar A
def generate_person():
    chosen_person = data[randint(0, len(data) - 1)]
    name = chosen_person['name']
    followers = chosen_person['follower_count']
    description = chosen_person['description']
    country = chosen_person['country']
    return [name, followers, description, country]


def biggest_number(num1, num2):
    biggest_number = [num1, 0]
    if num2 > num1:
        biggest_number = [0, num2]
        return biggest_number
    return biggest_number


def game():
    game_over = False
    score = 0
    count = 0
    while game_over == False:
        print(logo)
        if score > 0:
            print(winner_phrase)
        elif score == -1:
            print(f"Sorry, that's wrong. Final score: {game_over_score}")
            game_over = True
            break
        if count == 0:
            a = generate_person()

        b = generate_person()
        while a == b:
            b = generate_person
        print(f"Compara A: {a[0]}, a {a[2]}, from {a[3]}")
        print(vs)

        print(f"Against B: {b[0]}, a {b[2]}, from {b[3]}")
        answer = input("Who has more followers? [A] or [B]\t").lower()

        biggest = biggest_number(a[1], b[1])

        if biggest[1] == 0:
            higher_followers = a
            compare = b
        else:
            higher_followers = b
            compare = a

        count += 1

        if compare <= higher_followers:
            game_over_score = score
            score = -1
            clear()
        else:
            score += 1
            a = b
            winner_phrase = f"You're right. Current score: {score}"
            clear()


game()

''' print(vs)
for e in (lista):
  print(e) '''