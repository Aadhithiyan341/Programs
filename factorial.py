def factorial(n):
    # If the number is 0 or 1, return 1 (base case)
    if n == 0 or n == 1:
        return 1
    # Calculate factorial by recursion
    else:
        return n * factorial(n - 1)

# Input from the user
number = int(input("Enter a number to calculate its factorial: "))

# Ensure the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
