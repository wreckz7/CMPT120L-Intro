#Test 3 List Questions 1-5.py
#This program will perform the list methods to each list.
#by Awais Razaque 12/8/23

def Question1():
    print("Question 1:")
    aList = [123, 'xyz', 'zara', 'abc']
    aList.append("Shell")
    print(aList)
    print()

def Question2():
    print("Question 2:")
    aList = ['xyz', 'abc', 123]
    bList = ['me', 'myself', 'I']
    print(aList + bList)
    print()

def Question3():
    print("Question 3:")
    aList = [123, 'xyz', 'zara', 'abc']
    aList.insert(1, 2009)
    print(aList)
    print()

def Question4():
    print("Question 4:")
    aList = [123, 'xyz', 'zara', 'abc']
    print("The index of 'zara' is:", aList.index('zara'))
    print()

def Question5():
    print("Question 5:")
    aList = [123, 'xyz', 'zara', 'abc']
    string1 = aList.pop(0)
    print("The updated list is: ", aList)
    print("And the variable string1 is storing: ", string1)
    print()

def main():
    print("Welcome to this program! This program will perform the list methods to each list.")
    print()
    Question1()
    Question2()
    Question3()
    Question4()
    Question5()
    print("The program is over and has completed every list question 1-5!")
    input("Press <Enter> to exit the program!")
    
main()
