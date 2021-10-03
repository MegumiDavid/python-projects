from replit import clear
from art import logo
import random


def deal_cards(someone_cards_deck):
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    selected_card = random.choice(cards)
    someone_cards_deck.append(selected_card)
    return someone_cards_deck


def calculate_score(cards_list):
    """Take a list of cards and return the score calculated from the cards"""
    total_score = 0
    for score in cards_list:
        total_score += score

    if total_score == 21 and len(cards_list) == 2:
        return 0

    elif 11 in cards_list and total_score > 21:
        total_score -= 10

    return total_score


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "\tDraw 🙃"

    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"

    elif user_score == 0:
        return "Win with a Blackjack 😎"

    elif computer_score > 21 and user_score <= 21:
        return "\tOpponent went over. YOU WIN 😁"

    elif user_score > 21 and computer_score <= 21:
        return "\tYou went over. YOU LOOSE 😭"

    elif user_score > computer_score:
        return "\tYOU WIN 😃"

    elif user_score < computer_score:
        return "\tYOU LOOSE 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    print(logo)

    for c in range(2):
        deal_cards(user_cards)
        deal_cards(computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        print()

        if user_score > 21 or computer_score > 21 or user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            next_card = input("Type 'y' to get another card, type 'n' to pass:\t")
            if next_card == 'y':
                deal_cards(user_cards)
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        deal_cards(computer_cards)
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
