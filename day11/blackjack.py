# Blackjack

import art
import os
import random

# Deal Card


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculate Card Score


def calculate_score(cards):

    # has blackjack return 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # if ace exist and card score > 21 change value to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Get Winner by comparing with user score and computer score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Blackjack Main Program


def blackjack():

    user_cards = []
    computer_cards = []

    game_over = False

    os.system("cls")
    print(art.logo)

    # Add Cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"Your cards: {user_cards}, current score: {user_score}")
        print(
            f"Computer's first card: {computer_cards[0]}")

        if (user_score == 0 or computer_score == 0 or user_score > 21):
            game_over = True
            break
        else:
            should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


# Main
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()
