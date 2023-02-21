# Tip Calculator
print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = total_bill * (tip_percentage / 100)
pay_share = (total_bill + total_tip) / people

final_amount = round(pay_share,2)
final_amount = "{:.2f}".format(pay_share)

print(f"Each person should pay ${final_amount}")