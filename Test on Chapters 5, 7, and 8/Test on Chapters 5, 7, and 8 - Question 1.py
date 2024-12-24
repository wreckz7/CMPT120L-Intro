#Test on Chapters 5, 7, and 8 - Question 1.py
#This program will print the total price of the ice cream you select from the choices: Hard, Soft, and ND for Non-Diary. (Rounded to 2 decimal places)
#by Awais Razaque 11/3/23

def main():
    print("Welcome to this program!")
    print("This program will print the total price of the ice cream you select from the choices: Hard, Soft, and ND for Non-Diary. (Rounded to 2 decimal places)")
    print()
    while True:
        choiceoficecream = input("What type of ice cream would you like? \nType 'H' for Hard\nType 'S' for Soft\nType ND for Non-Diary\nYour Answer: ").lower()
        if choiceoficecream == "h":
            icecream = "Hard"
            totalprice = 2
            break
        elif choiceoficecream == "s":
            icecream = "Soft"
            totalprice = 3
            break
        elif choiceoficecream == "nd":
            icecream = "Non-Diary"
            totalprice = 4
            break
        else:
            print("That is an invalid option!")
            print()
    print()
    print("The total price of your choice of", icecream + " is: $ ", round(totalprice, 2))
    print()
    print("Thank you for using this program!")
    input ("Press <Enter> to end this program!")

main()
    
