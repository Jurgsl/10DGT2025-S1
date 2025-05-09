# Inputs and loops
# Juergen Lier
# 9 May 2025
# Version 2

# Ask the user a question and store their answer in a variable
# Ask the user for their name and store it
name = input("Kia ora, what is your name? ") # Stores answer as a string
print() # This adds a line break

# Test that input was stored correctly
print(f"Nice to meet you, {name}\n") # The \n adds a line break

# to comment code out, use ctrl + /

# Ask the user for two numbers and then add them together.
num1 = int(input("What is your first number please? "))
num2 = int(input('What is your second number? '))
print(f"You entered your first number as {num1}")
print(f"You entered your second number as {num2}")

# Adding the two answers together
sum = num1 + num2
print(f"The two numbers added together will result in {sum}")

# Multiplying the two inputs together
multiply = num1 * num2
print(f"The two numbers multiplied will result in {multiply}")


