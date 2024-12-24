#Test on Chapters 5, 7, and 8 - Question 2.py
#"This program will print the total bill (rounded to 2 decimal places) at a candy store depending on if you buy either a Candy Bar, Pack of Gum, or Trail Mix.
#by Awais Razaque 11/3/23

def main():
        print("Welcome this this program!")
        print("This program will print the total bill (rounded to 2 decimal places) at a candy store depending on if you buy either a Candy Bar, Pack of Gum, or Trail Mix.")
        print()
        print("Welcome to the Candy Store! Your items to choose from are:\n1) Candy Bar: $2\n2) Pack of Gum: $1\n3) Trail Mix: $3")
        totalbill = 0
        itemcount = 0
        print()
        while True:
                itemnumber = input("What is the item number (1, 2, or 3) of the item you wish to add to your total bill? Or type 'quit' to end the program and recieve your total bill: ").lower()
                if itemnumber == "1":
                        totalbill = totalbill + 2
                        itemcount = itemcount + 1
                elif itemnumber == "2":
                        totalbill = totalbill + 1
                        itemcount = itemcount + 1
                elif itemnumber == "3":
                        totalbill = totalbill + 3
                        itemcount = itemcount + 1
                elif itemnumber == "quit":
                        print("You will be paying for", itemcount, "item(s) and your total amount due is: $ ", round(totalbill, 2))
                        break
                else:
                        print("The item number you entered is invalid!")
        print()
        print("Thank you for using this program!")
        input ("Press <Enter> to end this program!")
main()
    
