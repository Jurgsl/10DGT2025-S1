# Demonstrate how to use while loops and if statements
# Juergen Lier
# 9 May 2025
# Version 1

# While loop
keep_going  = "" # The variable contains an empty string
while keep_going == "":

    like_coffee = input("Do you like coffee?")

    if like_coffee == "yes":
        print("That is great. I like coffee too!")
        keep_going = "finished"

    if like_coffee == "no":
        print("You are missing out. Why not give it a try.")
        keep_going = "finished"