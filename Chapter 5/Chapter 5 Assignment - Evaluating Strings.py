#Evaluating Strings.py
#This program will run a program that will create a userid using the first character of the user's (your) first name, plus the first 7 characters of the last name and another program which will print out the date in a full sentence from the format mm/dd/yyyy.
#by Awais Razaque 10/3/23

def main():
    print("Welcome to these two programs!")
    print("This first program will create a userid using the first character of the user's (your) first name, plus the first 7 characters of the last name.")
    print()
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ")
    print("Your userid is:", firstname[0].lower() + lastname[0:7].lower())
    print()
    print("This second program will print out the date in a full sentence from the format mm/dd/yyyy.")
    date = input("What is the date in the format (mm/dd/yyyy | 02/19/2019)? ")
    monthStr, dayStr, yearStr = date.split("/")

    #Using If's (Commented Out)
    """
    datesplit = date.split("/")
    if datesplit[0] == "01":
        month = "January"
    elif datesplit[0] == "02":
        month = "February"
    elif datesplit[0] == "03":
        month = "March"
    elif datesplit[0] == "04":
        month = "April"
    elif datesplit[0] == "05":
        month = "May"
    elif datesplit[0] == "06":
        month = "June"
    elif datesplit[0] == "07":
        month = "July"
    elif datesplit[0] == "08":
        month = "August"
    elif datesplit[0] == "09":
        month = "September"
    elif datesplit[0] == "10":
        month = "October"
    elif datesplit[0] == "11":
        month = "November"
    else:
        month = "December"
    """
    #

    #Proper Way
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]
    
    #print("The date selected is:", month + " " + datesplit[1] + "," + " " + datesplit[2] + ".")
    print("The date selected is:", monthStr + " " + dayStr + "," + " " + yearStr + ".")
    print()
    print ("Thank you for using this program.")
    input ("Press <Enter> to end this program!")
   
main()
