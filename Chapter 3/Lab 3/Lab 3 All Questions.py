#Lab 3 All Questions.py
#by Awais Razaque 9/15/23

from math import *
print ()
print ("Discussion Questions\nQuestion 1:")
print (4.0 / 10.0 + 3.5 * 2)
print (10 % 4 + 6 / 2)
print (abs(4 - 20 // 3) ** 3)
#1d) print (sqrt(4.5 - 5.0) + 7 * 3)
print ("Question 1d results in an error because you cannot take the sqrt of a negative number becaue it will then be imaginary.")
print (3 * 10 // 3 + 10 % 3)
print (3 ** 3)
print()

print ("Question 4:")
for i in range(1,11):
    print(i*i)
print ()
for i in [1,3,5,7,9]:
    print (i, ":", i ** 3)
print (i)
print ()
x = 2
y = 10
for j in range (0, y, x):
    print (j, end="")
    print (x+y)
print ("done")
print ()
ans = 0
for i in range(1,11):
    ans = ans + i * i
    print (i)
print (ans)
print ()

print ("Question 6:")
print (-10 // 3)
print (-10 % 3)
print (10 // -3)
print (10 % -3)
print (-10 // -3)
print ()

print ("Programming Exercises\nQuestion 2:")
diameter = eval(input("What is the size of the pizza? "))
price = eval(input("What is the price of the pizza? "))
radius = diameter/2
area = pi * (radius ** 2)
print ("The area is", area)
price_per_square_inch = price / area
print ("And the price per square inch is:", round(price_per_square_inch,2))
print ()

print ("Question 10:")
height = eval(input("What is the height of the building? "))
degrees = eval(input("What is the angle in degrees that the ladder makes with the building? "))
radians = (pi/180) * degrees
print ("The angle in degrees converted to radians is: ", radians)
length = height / (sin(radians))
print ("The length of the ladder is: ", round(length,0))
print ()

print("Thank you for using this program!")
input("Press the <Enter> key to quit the program.")

               

