# Demonstrate how to use while loops and if statements
# Juergen Lier
# 9 May 2025
# Version 2

# While loop
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
keep_going = ""
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
   

    


    