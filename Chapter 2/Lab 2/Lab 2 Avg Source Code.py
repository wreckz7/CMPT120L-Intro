# avg2.py
#   A simple program to average two exam scores  
#   Illustrates use of multiple input

def main():
    #Introduction
    #I coded this program to be able to calculate the average score of any number of exams!
    print("Welcome to this program!\nThis program computes the average of any amount of exam scores.")
    print()
    print("The input to the program will come from the user aka you. You will be inputting:\n* the number of exam scores you want to average\n* the scores of each exam")
    print("The output of the program will be the average of all the exam scores you entered.") 
    print()
    
    numberofexams = eval(input("How many exam scores do you want to find the average of? "))
    sumofexams = 0
    for i in range (numberofexams):
        examscore = eval(input("What is the exam score? "))
        sumofexams = sumofexams + examscore
    average = sumofexams/numberofexams

    print("The average of the", numberofexams, "exam(s) is:", average)
    print()
    print("Thank you for using this program!")
    input("Press the <Enter> key to quit the program.")

main()
