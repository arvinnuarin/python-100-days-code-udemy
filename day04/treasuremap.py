# Treasure map

row1=  ["๐", "๐", "๐คจ"]
row2 = ["๐", "๐ซต", "๐"]
row3 = ["๐ถ", "๐ฒ", "๐ป"]

map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = "X"

print(map)

