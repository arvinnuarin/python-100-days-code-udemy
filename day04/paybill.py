# Who will pay the bill
import random

names_string = input("Give me everybody's name, separated by a comma.\n")

names = names_string.split(",")
# manual
random_index = random.randint(0, len(names)-1)  
billpayer = names[random_index]

print(f"{billpayer} is going to buy the meal today!")

# using choice method
billpayer = random.choice(names)

print(f"{billpayer} is going to buy the meal today!")
