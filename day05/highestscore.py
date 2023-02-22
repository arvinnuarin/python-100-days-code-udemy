# Highest Score

student_scores = input("Input a list of student score: ").split()

# using max and min

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(max(student_scores))
print(min(student_scores))

# using loop
highest = 0

for n in student_scores:
    if int(n) > highest:
        highest = int(n)

print(f"The highest score in the class is: {highest}")