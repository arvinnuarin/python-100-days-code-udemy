# BMI Calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in m: ")

bmi = float(weight) / (float(height) ** 2)

print(int(bmi))