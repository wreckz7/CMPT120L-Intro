#Lab 7 All Questions.py
#This program goes through all of lab 7 and goes through the programming exercise #1.
#by Awais Razaque 10/6/23

def main():
    print("Welcome to this program!\nThis program goes through all of lab 7 and goes through the programming exercise #1.")

    n = int(input("Number? "))
    if n < 0:
        print("The absolute value of", n, "is", -n)
    else:
        print("The absolute value of", n, "is", n)
    print()

    a = 0
    while a < 10:
        a = a + 1
        if a > 5:
            print(a, ">", 5)
        elif a <= 3:
            print (a, "<=", 3)
        else:
            print ("Neither test was true")
    print()

    #This Program Demonstrates the use of the == operator
    #using numbers
    print(5 == 6)
    #Using variables
    x = 5
    y = 8
    print(x == y)
    print()

    #high_low.py
    #Plays the guessing game higher or lower

    #This should actually be something that is semi random like the
    #last digits of the time or something else, but that will have to
    #wait till a later lab.
    number = 7
    guess = -1

    print("Guess the number!")
    while guess != number:
        guess = int(input("Is it... "))

        if guess == number:
            print ("Hooray! You guessed it right!")
        elif guess < number:
            print ("It's bigger...")
        elif guess > number:
            print("It's not so big.")
    print()

    #even.py
    #Asks for a number.
    #Prints if it is even or odd

    number = float(input("Tell me a number: "))
    if number % 2 == 0:
        print(int(number), "is even.")
    elif number % 2 == 1:
        print(int(number), "is odd.")
    else:
        print(number, "is very strange.")
    print()

    #average1.py
    #keeps asking for numbers until 0 is entered.
    #Prints the average value.

    count = 0
    sum = 0.0
    number = 1 #set to something that will not exit the while loop immediately.

    print("Enter 0 to exit the loop")

    while number != 0:
        number = float(input("Enter a number: "))
        if number != 0:
            count = count + 1
            sum = sum + number
        if number == 0:
            print ("The average was:", sum/count)
    print()

    print("Programming Exercise #1:")
    print("This program will calculate the total wages for the week including overtime hours over 40 from the user entering the number of hours worked and the hourly rate.")
    print()
    hrsworked = eval(input("What is the number of hours worked? "))
    hourlyrate = eval(input("What is the hourly rate? "))
    if hrsworked > 40:
        overtimehrs = hrsworked - 40
        totalwages = (hourlyrate * 40) + (hourlyrate * (1.5 * overtimehrs))
    else:
        totalwages = hourlyrate * hrsworked
    print("Total wages for the week: ", totalwages, "dollars.")
    print()
    
    print ("Thank you for using this program.")
    input ("Press <Enter> to end this program!")

main()
