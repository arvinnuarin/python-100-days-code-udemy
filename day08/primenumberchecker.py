# Prime Number Checker
n = int(input("Check this number: "))

def prime_checker(number):
    isprime = True

    for n in range(2, number):
        if number % n == 0:
           isprime = False
           break

    if isprime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

prime_checker(n)
