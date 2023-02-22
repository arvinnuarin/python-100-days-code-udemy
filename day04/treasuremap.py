# Treasure map

row1=  ["😀", "🙃", "🤨"]
row2 = ["👋", "🫵", "🙏"]
row3 = ["👶", "👲", "👻"]

map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = "X"

print(map)

