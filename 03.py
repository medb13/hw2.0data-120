'''
# --------------------------------------- #
#            3: DATA STRUCTURES           #
# --------------------------------------- #
Slides to reference: 2.5 Data Structures and String Manipulation

In this problem, you will practice using 3 types of data structures:
      - Lists are ordered collections of items that can be resized and hold multiple datatypes.
      - Dictionaries are a mutable collection of key value pairs that map a unique, immutable key onto some value.
      - Sets are mutable sets of immutable, unique, and unordered elements.
'''
print("-------- Problem 3 --------")
# Write a program that takes a pizza order and outputs the order and the price of the order.
# Pizzas are priced as follows:
# Small pizzas start at $5, medium pizzas start at $8, and large pizzas start at $10.
# The customer can add as many toppings as they would like, and they are priced as follows:
#       $0.50: Corn, Onions, Bell Peppers, Olives
#       $1.00: Spinach, Mushrooms, Anchovies, Pineapple
#       $1.50: Pepperoni, Sausage, Chicken, Ham

# First, prompt the user to input their desired pizza size. Then, prompt them to enter their toppings.
# You can assume that the pizza size and toppings will be valid (e.g. toppings won't be numbers).
# Toppings will be entered as a list delimited by commas and spaces (", ").
# Your customers are forgetful and may accidentally order the same topping twice.
# However, you should not charge them twice! Each topping may only be added once!
# Sample input:
#     Medium
#     Onions, Mushrooms, Olives, Ham, Spinach, Mushrooms, Corn
# Sample output:
#     You ordered a medium pizza with 6 topping[s]. Your total is $13.00.
### CODE GOES HERE, MAKE SURE TO COMMENT!###


# dictionaries for the pizza price by size and additional toppings
pizza_prices = {
    "small": 5,
    "medium": 8,
    "large": 10
}

topping_prices = {
    "corn": 0.50, "onions": 0.50, "bell peppers": 0.50, "olives": 0.50,
    "spinach": 1.00, "mushrooms": 1.00, "anchovies": 1.00, "pineapple": 1.00,
    "pepperoni": 1.50, "sausage": 1.50, "chicken": 1.50, "ham": 1.50
}
# asks user for pizza size first, then toppings, storing both inputs
size = input("enter pizza size: ").lower()

toppings = input("enter pizza toppings : ").lower()

# sets total for later use with for loop
total = pizza_prices[size]

# creates a list out of the toppinbgs input
toppings_list = toppings.split(", ")

#creates a set to remove duplicates from the list
toppings_set = set(toppings_list)

#adds up the price of the toppings
for topping in toppings_set:
    total += topping_prices[topping]

# for formatting in the outp[ut
toppings_count = len(toppings_set)

print(f" You ordered a {size} pizza with {toppings_count} topping[s]. Your total is ${total:.2f}.")
      


