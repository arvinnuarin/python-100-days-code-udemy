# Leap Year
# normal year = 365 days, leap year = 366

# 2000 / 4 = 500 (leap)
# 2000 / 100 = 20 (Not Leap)
# 2000 / 400 = 5 (Leap)


year = int(input("Which year do you want to check? "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is LEAP year.")
else:
    print(f"{year} is NOT LEAP year.")
 