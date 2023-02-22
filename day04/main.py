# Randomization
import random
import my_module

# random integer from 1 to 10
random_integer = random.randint(1,10)

print(random_integer)

print(my_module.pi)

random_float = random.random()

print(random_float)


# Lists
states_of_america = ["Delaware", "Pennyslvania"]

print(states_of_america[0])

states_of_america.append("New York")

#Lists in a list

fruits = ["Strawberriers", "Nectarines"]
vegetables = ["Spinach", "Kale"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)