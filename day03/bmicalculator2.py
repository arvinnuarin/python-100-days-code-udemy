# BMI Calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in m: ")

bmi = round(float(weight) / (float(height) ** 2))

result = ""

if bmi < 18.5:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 30:
    result = "overweight"
elif bmi < 35:
    result = "obese"
else:
    result = "clinically obese"

print(f"Your BMI is {bmi}, you are {result}.")


