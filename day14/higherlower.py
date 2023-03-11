# Higher Lower
import art
import game_data
import random
import os


# Logo
print(art.logo)

# Compare to get who has more followers


def compare(compare_a, compare_b):
    a_followers = compare_a["follower_count"]
    b_followers = compare_b["follower_count"]

    if (a_followers > b_followers):
        return "A"
    elif (a_followers < b_followers):
        return "B"
    else:
        return "AB"


# Game Function
def game():
    # clear screen
    os.system("cls")
    # get random choice for comparison
    score = 0
    is_game_over = False
    compare_a = random.choice(game_data.data)

    while not is_game_over:

        if score > 0:
            print(f"You're right! Current Score: {score}")

        print(
            f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']} ")

        print(art.vs)

        compare_b = random.choice(game_data.data)

        print(
            f"Compare B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']} ")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Incorrect Input
        if (choice not in ('A', 'B')):
            exit(0)

        # Get Result
        result = compare(compare_a, compare_b)

        if (result == "AB"):
            print(f"They have same followers. Final Score: {score}")
            break

        # Correct
        if result == choice:
            is_game_over = False
            score += 1
            compare_a = compare_b
        else:
            is_game_over = True
            os.system("cls")
            print(f"Sorry, that's wrong. Final Score: {score}")


game()
