# Life in Weeks
#1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# Create a program using maths and fstring that tell us how many days, weeks, months we have lfet if we live until 90 years old.

age = input("What is you current age? ")

remaining_year = 90 - int(age)

months = remaining_year * 12
weeks = remaining_year * 52
days = remaining_year * 365

print(f"You have {days} days, {weeks} weeks, {months} months left.")