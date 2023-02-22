# Average Student Height

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# solution 

total_height = sum(student_heights)
students = len(student_heights)
average = round(total_height / students)

print(average)

# using loop

sumheight = 0
counter = 0

for n in student_heights:
    sumheight += int(n)
    counter+=1

average = round(sumheight / counter)

print(average)