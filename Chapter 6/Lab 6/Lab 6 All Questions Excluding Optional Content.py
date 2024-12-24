#Lab 6 All Questions.py
#This program completes the tutorial for Lab 6 - Functions, creating a marist username and a password that is at least 8 characters long and a password that contains both upper and lower case characters.
#by Awais Razaque 10/27/23

#CMPT 120 Intro to Programming
#Lab #5 - Working with Strings and Functions
#Author: Awais Razaque
#Created: 2023-10-27

def getfullname():
    print()
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last

def maristusername(first, last):
    maristusername = first + "." + last
    return maristusername.lower()

def passwordcheck():
    while True:
        print()
        passwd = input("Create a new password: ")
        if len(passwd) >= 8 and passwordstrength(passwd) == True:
            print("Congrats, the password you entered is long enough and has both upper and lower case characters!")
            break
        elif len(passwd) < 8 or passwordstrength(passwd) == False:
            print("The password is too short or does not have both upper and lower case characters!")
            print("Reminder: Your password must be at least 8 characters long and contain both upper and lower case characters.")
    return passwd

def passwordstrength(passwd):
    if any(i.islower() for i in passwd) and any(i.isupper() for i in passwd):
        passwordstrong = True
    else:
        passwordstrong = False
    return passwordstrong
            
def main():
    print("Welcome to this program!")
    print("This program completes the tutorial for Lab 6 - Functions, creating a marist username and a password that is at least 8 characters long and a password that contains both upper and lower case characters.")
    first,last = getfullname()
    
    username = maristusername(first, last)
    print()
    print("Your username will be: " + username)

    passwd = passwordcheck()
    print()
    print("Account configured. Your new email address is", username + "@marist.edu")
    print()
    print("Thank you for using this program!")
    input("Press <Enter> to end this program!")

main() 
