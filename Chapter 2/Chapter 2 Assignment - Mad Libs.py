# madlib.py
# A program to construct an amusing sentence from four different words entered by the user.
# by Awais Razaque 9/11/23

def main():
    #Introduction
    print("Welcome to this program! This program will construct an amusing sentence from four words that you will enter.")
    print()
    noun = input("Enter a noun - \na word that represents a person, thing, concept, or place: ")
    verb = input("Enter a verb - \n a word that indicates a physical action, a mental action, or a state of being: ")
    adjective = input("Enter an adjective - \na word that modifies or describes a noun or pronoun: ")
    place = input("Enter a place - \na location: ")
    print()
    print("In the beginning of the week we will be going to the", place, "to visit the", adjective, noun, "as it", verb,"(s).")
    print()
    #Ending/Loop
    print("Thank you for playing this program!")
    againloop = input("Do you want to play again? (y/n) ")
    if againloop == "Y":
        print()
        main()
    elif againloop == "y":
        print()
        main()
    else:
        print()
        print("Thank you for playing this program!")
        input("Press the <Enter> key to quit the program.")
        
main()
