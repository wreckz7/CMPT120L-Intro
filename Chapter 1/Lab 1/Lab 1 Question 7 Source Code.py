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
    a = eval(input("Enter another number between 0 and 1 (Calculation 1):"))
    b = eval(input("Enter another number between 0 and 1: (Calculation 2):"))
    c = eval(input("Enter another number between 0 and 1: (Calculation 3):"))
    for i in range(100):
        a = 3.9 * a * (1 - a)
        b = 3.9 * (b - b * b)
        c = 3.9 * c - 3.9 * c * c
        print (a , b , c)

main()

