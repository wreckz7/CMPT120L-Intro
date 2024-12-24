#Lab 13 Recursion.py
#This program will complete the tutorial for the Chapter 13 Lab: Recursion.
#by Awais Razaque 11/17/23

print("Welcome to this program!")
print("This program will complete the tutorial for the Chapter 13 Lab: Recursion.") 
print()

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

'''
def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)

deliver_presents_iteratively()
'''

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)

print()

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))

print()

'''
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

print(sum_recursive(1,0))
'''

# Global mutable state
current_number = 1
accumulated_sum = 0


def sum_recursive():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()

print(sum_recursive())

print()

def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        print(smaller_list)
        return head + list_sum_recursive(smaller_list)

list_sum_recursive([1, 2, 3])

print()

def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(5))

print()
print("Thank you for using this program!")
input ("Press <Enter> to end this program!")
