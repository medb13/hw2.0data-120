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

# prompt user to input two numbers

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

# ensure valid range
while num1 > num2:
    print("invalid range, first number must be smaller than the second.")
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))

# loop through numbers in range
for num in range(num1, num2 + 1):
    
    # assume number is prime
    is_prime = True
    
    # numbers less than 2 are not prime
    if num < 2:
        is_prime = False
    
    # check divisiblity
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    
    # print if prime
    if is_prime:
        print(num, end = " " )
