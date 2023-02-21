# Love Calculator
print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = (name1 + name2).lower()

count_t = combined_name.count("t")
count_r = combined_name.count("r")
count_u = combined_name.count("u")
count_e = combined_name.count("e")

count_l = combined_name.count("l")
count_o = combined_name.count("o")
count_v = combined_name.count("v")

score_true = count_t + count_r + count_u + count_e
score_love = count_l + count_o + count_v + count_e

score = int(str(score_true) + str(score_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")  