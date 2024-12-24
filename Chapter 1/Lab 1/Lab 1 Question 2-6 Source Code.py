# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print for the original calculation? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 2.0 * x * (1 - x)
        print(x)
    print ("Original Calculation has finished...")

def calculation1():
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * x * (1 - x)
        print (x)
    print ("Calculation 1 has finished...")

def calculation2():
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * (x - x * x)
        print (x)
    print ("Calculation 2 has finished...")

def calculation3():
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * x - 3.9 * x * x
        print (x)
    print ("Calculation 3 has finished...")


main()
calculation1()
calculation2()
calculation3()
