# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    #Introduction
    print("Welcome to this program!\nThe purpose of this program is to convert a Celsius temperature of the users choosing to an equivalent Fahrenheit temperature.")
    print()
    print("The input to this program will come from the user aka you. You will be inputting\n* a Celsius temperature you wish to convert to Fahrenheit")
    print("The output of the progrom will be the correct converted Fahrenheit temperature from the Celsius temperature you entered.")
    print()
          
    for i in range (5):
        celsius = eval(input("What is the Celsius temperature you wish to convert? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print()
    print()
    print("Thank you for using this program!")
    input("Press the <Enter> key to quit the program.")

main()
