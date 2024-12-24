#Lab 8 All Questions.py
#This program goes through all of lab 8 consisting of the looping tutorial, all 6 screen captured examples and the exercise that prints out asterisks with the blanks filled in.
#by Awais Razaque 10/13/23

def main():
    print("Welcome to this program!\nThis program goes through all of lab 8 consisting of the looping tutorial, all 6 screen captured examples and the exercise that prints out asterisks with the blanks filled in.")
    print()
    print("How To Make a While Loop in Python:")
    # Take user input
    number = 2

    # Condition of the while loop
    while number < 5:
        print("Thank you")
        # Increment the value of the variable "number by 1"
        number = number +1

    print()
    
    # Take user input
    number = 2

    # Condition of the while loop
    while number < 5:
        # Find the mod of 2
        if number % 2 == 0:
            print("The number "+str(number)+" is even")
        else:
            print("The number "+str(number)+" is odd")


        # Increment 'number' by 1
        number = number +1

    print()

    print("While versus For Loops in Python:")
    # Take user input
    number = 2

    while number < 5:
        print("Thank you")
        #Increment 'number' by 1
        number = number + 1

    print()

    # Print "Thank you" 3 times
    for number in range(3):
        print("Thank you")

    print()
    
    #Print the below statement 3 times
    for number in range(3):
        print("-------------------------------------------")
        print("I am outer loop iteration "+str(number))
        #Inner loop
        for another_number in range(5):
            print ("****************************")
            print ("I am inner loop iteration "+str(another_number))

    print()

    print("Construct the following pattern, using a nested for loop:")
    #Initialize for first five rows
    n = 5

    #Start the loop to print the first five rows
    for i in range(n):
        for j in range(i):
            print('* ', end="")
        print(' ')

    #Start the loop to print the remaining rows in decreasing order of stars
    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

    print()

    print("break continue Keywords: Creating Infinite Loops")
    # Take user input
    number = 2

    # Condition of the while loop
    while number < 5:
        # condition of the nested while loop
        while number % 2 == 0:
            print("The number "+str(number)+" is even")
            break


        number += 1

    print()

    infiniteloopanswer = input("The last code segment of this lab is an infinite loop, do you wish to continue? (y/n) : ").lower()
    if infiniteloopanswer == "y" or infiniteloopanswer == "Y": #just to make sure both lower/upper case work, since I dont want to test it myself even though I put .lower() before
        # Take user input
        number = 2

        while number < 5:
            while number % 2 == 0:
                print("The number "+str(number)+" is even")
                break
            continue


            number += 1
    else:
        print()
        print ("Infinite Loop has not been ran, but it is in the source code to see!")

    print()
    print ("Thank you for using this program.")
    input ("Press <Enter> to end this program!")
    
main()
