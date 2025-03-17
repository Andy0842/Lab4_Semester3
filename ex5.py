#Enter a number and output its factorial by a for loop.
#Auther: Yang Yue

# This program calculates the factorial of a number using a for loop

def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Get input from the user
try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(number)
        print(f"The factorial of {number} is {result}.")
except ValueError:
    print("Please enter a valid non-negative integer.")
