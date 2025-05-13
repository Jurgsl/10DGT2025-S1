# Demonstrate how to create function, thus making my recyclable.
# Juergen Lier
# 14 May 2025
# Version 3

# While loop
# Version 1
'''keep_going  = "" # The variable contains an empty string
while keep_going == "":

    like_coffee = input("Do you like coffee?")

    if like_coffee == "yes":
        print("That is great. I like coffee too!")
        keep_going = "finished"

    if like_coffee == "no":
        print("You are missing out. Why not give it a try.")
        keep_going = "finished"
        '''

# Version 2. Making the program more pythonic.
'''keep_going = ""
while keep_going == "":
    # .lower converts the answer to lower case
    like_coffee = input("Do you like coffee?").lower() 
    if like_coffee == "yes" or like_coffee == 'y':
        print("That is great. I like coffee too!")
    
    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out!")

        like_tea = input("Do you like tea instead?").upper()

        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try :)")
        elif like_tea == "NO" or like_tea == "N":
            print("I am sorry. That is all I have for now.")
        else: 
            print("I don't understand. Please answer with either Yes or No.")

    else: 
        print("I don't understand. Please answer with either Yes or No.")

    keep_going = input("Press <enter> to continue or any other key to quit.")
   '''

# Version 3
# Create a function that I can use over and over again.
# Makes my code recyclable.
# The program will ask a person for a number and do something with it.
# Loop the program until a valid number gets entered. 

'''def intcheck(): # def creates a function. intcheck is the function name.
    valid = False
    while not valid:
        error = "Whoops, you have entered the wrong number. Please " \
        "enter a valid integer between 1 and 10."

        try:
            response = int(input("Enter and integer between 1 and 10: "))
            
            if response >=1 and response <=10:
                print(response)
                valid = True
            else: 
                print(error)

        except ValueError:
            print(error)


intcheck() # To call(use) the function, write out its name.
'''

# Version 3.1
# Create a function that I can use over and over again.
# Makes my code recyclable.
# The program will ask a person for a number and do something with it.
# Loop the program until a valid number gets entered. 

def intcheck(question, low, high): # def creates a function. intcheck is the function name.
    valid = False
    while not valid:
        error = f"Whoops, you have entered the wrong number. Please " \
        f"enter a valid integer between {low} and {high}."

        try:
            response = int(input(f"Enter and integer between {low} and {high}: "))
            
            if low <= response <= high:
                print(f"You have entered {response}.")
                valid = True
            else: 
                print(error)

        except ValueError:
            print(error)
    return response

# Questions to ask the user
num1 = intcheck("Enter a number between 1 and 10", 1, 10) # To call(use) the function, write out its name.
num2 = intcheck("Enter a number between 15 and 20", 15, 20)
# print(num1) # Used to check for correct storage.
#adding the responses together
sum_num = num1 + num2

# multiply the responses
multiply = num1 * num2 

print(f"Your two numbers added together are {sum_num}.")
print(f"Your two numbers multiplied result in {multiply}.")