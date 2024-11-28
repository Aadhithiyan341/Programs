def is_prime(number):
    # Check if number is less than 2
    if number <= 1:
        return False
    
    # Check divisibility from 2 to square root of number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Input from the user
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
