'''
# --------------------------------------- #
#           4: FUNCTION PRACTICE          #
# --------------------------------------- #
Slides to reference: 2.6 Functions

In this problem, you will practice writing and using functions.
Functions allow us to break code into reusable blocks and return useful values.

You will be writing two functions:
    - One to check if a password meets common strength requirements.
    - One to interact with the user and validate their input.
'''

print("-------- Problem 4 --------")

# Part 1: is_valid_password(password)
# ----------------------------------------
# Write a function called `is_valid_password` that checks if a password is strong.
# A valid password must:
#    - Be at least 8 characters long
#    - Include at least one uppercase letter
#    - Include at least one lowercase letter
#    - Include at least one number
#
# If the password meets all requirements, return True.
# Otherwise, print at least one case it is failing and return False.
# If it fails multiple cases you can print one or all of the cases it is failing.
# You can assume the password will only contain upper/lowercase letters and/or numbers.
# Remember to write a docstring for the function!
### CODE GOES HERE, MAKE SURE TO COMMENT!###


# Part 2: password_helper()
# ----------------------------------------
# Write a function called `password_helper` that:
#   - Continuously (in a while loop) prompts the user to enter a password using input()
#   - This while loop should continue until the user enters the word "quit".
#    - You can check whether "quit" is a valid password,
#      you don't have to go out of your way to make sure you do not.
#   - Calls your is_valid_password() function
#   - Prints whether the password is valid or not.
# Sample input:
#   badpassword123
# Sample output:
#   Your password is missing an uppercase letter.
#   badpassword123 is NOT valid.
#
# This function does not return anything.
# You may assume the user enters a string.
# Remember to write a docstring for the function!
### CODE GOES HERE, MAKE SURE TO COMMENT!###


# Some extra code to run your functions, don't worry about it!
def main():
  password_helper()

if __name__ == "__main__":
    main()

def is_valid_password():
    """
    function to check if password is strong, meaning it must:
  - Be at least 8 characters long
  - Include at least one uppercase letter
  - Include at least one lowercase letter
  - Include at least one number
"""
    if len(password) < 8:
        print("your password must be at least 8 characters long.")
        return False
    # flags to track requirements
    has_upper = False
    has_lower = False
    has_number = False
    
    # loop through each character
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
            
    # checks through all requirements individiually
    if not has_upper:
        print("your password is missing an uppercase letter.")
        return False
    
    if not has_lower:
        print("your password is missing a lowercase letter.")
        return False
    
    if not has_number:
        print("your password is missing a number.")
        return False
     # if all checks pass, password is strong
    return True

    def password_helper():
    
    """
    asks the user to enter passwords until they type 'quit'
    checks if each password is valid and prints the result
    """
    
    #  asks the user for passwords continuously
    while True:
        password = input("enter a password (or type quit to stop): ")
        
        # if user inputs 'quit', break out of the loop
        if password == "quit":
            break
        
        # check if password is valid
        if is_valid_password(password):
            print(password + " is valid.")
        else:
            print(password + " is NOT valid.")
    
