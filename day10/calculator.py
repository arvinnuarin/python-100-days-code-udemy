# Calculator
import art
import os

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Operation Dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator(): 
    finished = False
    os.system("cls")
    print(art.logo)
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    while not finished:
            
        operator = input("Pick an operation: ")

        if (operator in operations):
            num2 = float(input("What's the next number? "))
        else:
            print("Invalid operation! Use only the symbol provided above.")
            break
        
        calculate = operations[operator]
        result = calculate(num1, num2)

        print(f"{num1} {operator} {num2} = {result}.")

        num1 = result # save the current result to num1 so it would iterate

        calcmore = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation or type 'x' to exit: ").lower()

        if(calcmore == "x"):
            finished = True
            break
        elif(calcmore != "y"):
            finished = True
            calculator()
            break

# Start calculator
calculator()
  






