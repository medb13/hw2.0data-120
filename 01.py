'''
# --------------------------------------- #
#            1: CONTROL FLOW              #
# --------------------------------------- #
Slides to reference: 2.4 Control Flow

In this problem, you will practice using two useful loops:
     - For loops use a counter to track iterations and run a set amount of times.
     - While loops run a variable amount of times based on a condition.

You aren't expected to use break/continue/pass in this particular problem but
they are useful, so be sure you know how to use them!
'''
print("-------- Problem 1 --------")
# Prompt the user to input two numbers. The numbers will be input on two different lines.
# The first number should be smaller than the second.
# (You should check if this is the case and prompt the user to enter a valid range if it is not.)
# Then, print all prime numbers between those two numbers, inclusive.
# Sample input:
#   5
#   11
# Sample output:
#   5 7 11
### CODE GOES HERE, MAKE SURE TO COMMENT!###

# Prompt the user to input two numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

# Ensure the first number is smaller than the second
while num1 > num2:
    print("invalid range, first number must be smaller than the second.")
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))

# Function to check if a number is prime
def prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for factors from 2 up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

prime(7)

# Loop through the range and print prime numbers
for num in range(num1, num2 + 1):
    if prime(num):
        print(num, end=" ")
