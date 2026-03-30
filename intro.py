# intro.py- your first program
#=====================================================================
# Program: intro.py
# What it does: Introduces you and remembers your info
#=====================================================================

# The print() function displays text on the screen
# Whatever you put inside the quotes gets printed
print("Welcome to your first Python Program!")
print("Let me get to know you.")
print("")  # This prints a blamk line

# The input() function asks a question and WAITS for you
# To type an answer. It saves whatever you type into
# The variable on the left side of the = sign
name = input("What is your name?")

# Now 'name' is a variable that holds your name
# Lets collect a few more pieces of information
age = input("How old are you?")
stroke = input("What is your best stroke?")
fish = input("What is your favorite fish to catch?")

# Now let's print everything back nicely
# Notice we can mix regular text with variables
print("")
print("Here is what I know about you:")
print("Name:", name)
print("Age:", age)
print("Best Stroke:", stroke)
print("Favorite fish:", fish)
print("")
print("Nice to meet you,", name + "!")
print("Now let's build something great.")