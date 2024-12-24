#Distance Formula.py
#This program will find the length of the hypotenuse between two order pairs in a right triangle using Pythagorean Theorem.
#by Awais Razaque 9/18/23

from math import *
def main():
    #Introduction
    print ("Welcome to this program!\nThis program will find the length of the hypotenuse between two order pairs in a right triangle using Pythagorean Theorem.")
    x1, y1 = eval(input("Please enter the first x and y pair, separated with a comma: "))
    x2, y2 = eval(input("Please enter the second x and y pair, separated with a comma: "))
    lengthleg1 = x2-x1
    lengthleg2 = y2-y1
    distance = sqrt((lengthleg1 ** 2) + (lengthleg2 ** 2))
    print ("The distance between the two points without rounding is", distance)
    print ()
    print ("The distance between the two points rounded to the nearest whole number is: ", round(distance))
    print ("The distance between the two points rounded to the nearest tenth is: ", round(distance,1))
    print ("The distance between the two points rounded up to the next whole number is: ", ceil(distance))
    print ()
    print("Thank you for using this program!")
    input("Press the <Enter> key to quit the program.")
    
main()
