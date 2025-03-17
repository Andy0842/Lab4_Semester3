#Enter a number and output its factorial by a while loop
#Auther: Yang Yue

# This program calculates the factorial of a number using a while loop

def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

# Get input from the user
try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        result = calculate_factorial(number)
        print(f"The factorial of {number} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
