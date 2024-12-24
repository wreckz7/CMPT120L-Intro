#Debugging Lab.py
#This program will fix all syntax and code errors in 3 sections of code! The changes made are in quotations in the source code!
#by Awais Razaquem 11/10/23

#Intro
print("Welcome to this program!")
print("This program will fix all syntax and code errors in 3 sections of code! The changes made are in quotations in the source code!")
print()

#Example 1: 

#There are at least 3 errors in the code below: 2 can probably be found
#by simply "eyeing" the code, the last one you may need to run the code to find it.

greeting = input("Hello, possible pirate! What's the password? ") #add closing quotation mark
if greeting == "Arrr!": #Get rid of (), make in to ==
    print("Go away, pirate.")
else: #change elif to else with colon after
    print("Greetings, hater of pirates!") #indent



#-------------------------------------------------------------
#Example 2: 

#At least 8 errors,
#First line of code (after comments) has 3 errors alone
#Some errors are repeated more than once.


# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = eval(input("Greetings! What is your year of origin? ")) #change == to =, change ' at end to ", change int.input to eval

if year < 1900: #change to just less than (<), add colon after if statement
    print ("Woah, that's the past!") #change ' ' to " "
elif year >= 1900 and year <= 2020: #change first sign to greater than or equal to (>=) and second sign to less than or equal to (<=), change && to and
    print ("That's totally the present!")
else: #change to else:
    print ("Far out, that's the future!!")




#---------------------------------------------------------------	
#Example 3: 
	
# Calculating Grades:

#At least 9 errors. Most are typos, but a few may take running the code and stopping at various spots to examine values.

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 34
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #add int(input

exam_three = int(input("Input exam grade three: ")) #change str to int, change exam_3 to exame_three

grades = [exam_one, exam_two, exam_three] #add commas between 
sum = 0
for grade in grades: #change second grade to grades
  sum = sum + grade

avg = sum / len(grades) #fix grdes to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #add colon at the end of elif statement
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #make it "C", not "C'
elif avg <= 69 and avg >= 60: #change second number from 65 to 60
    letter_grade = "D"
else: #change elif: to else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F": #change letter-grade to letter_grade, change is to ==
    print ("Student is failing.") #add ()
else:
    print ("Student is passing.") #add ()

print()
print("Thank you for using this program!")
input("Press <Enter> to quit this program!")
