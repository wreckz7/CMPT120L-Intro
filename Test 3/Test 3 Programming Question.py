#Test 3 Programming Question.py
#This program will create a dice game where you will play till you reach a score of 50 or till you lose all 3 of your lives.
#by Awais Razaque 12/8/23

def rules():
    print("Welcome to this program! This program will create a dice game where you will play till you reach a score of 50 or till you lose all 3 of your lives.")
    print()
    print("The rules on each role are:\nIf you roll an even number, then you will recieve the value of the roll doubled in points (Ex. a role of 2 will earn 2 x 2 or 4 points)\nIf you roll an odd number, then you will get the actual value of the dice or roll.\nLastly, if you roll a 6, you will lose 1 of your 3 lives.")
    print()
    print("Goodluck and Have Fun!")

def roll():
    global lives
    global score
    import random
    rollednum = random.randint(1,6)
    print("You rolled a:", rollednum)
    if rollednum == 2 or rollednum == 4:
        pointsearned = rollednum * 2
        score = score + pointsearned
        print("You rolled an even number. You have gained:", pointsearned ,"points!")
    elif rollednum == 1 or rollednum == 3 or rollednum == 5:
        score = score + rollednum
        print("You rolled an odd number. You have gained:", rollednum ,"points!")
    elif rollednum == 6:
        lives = lives - 1
        print("Since, you rolled a 6, you have now lost a life!")
    else:
        print("Invalid!")         

def main():
    restart = "Y"
    while restart == "Y":
        global lives
        global score
        score = 0
        lives = 3
        rules()
        while lives > 0:
            print()
            roll()
            if lives == 0:
                print()
                print("You have ran out of lives and have lost the Game! Sorry")
                break
            elif score >= 50:
                print()
                print("You have won the Game! Congratulations")
                break
            else:
                print("Your current score is:", score ,"and your number of lives remaining is:", lives)
        print()
        while True:
            restart = input("The program is now over! Do you wish to play again? (Y/N): ").upper()
            if restart == "N":
                print()
                print("Thank you for playing!")
                input("Press <Enter> to quit the program.")
                break
            elif restart == "Y":
                print("Restarting the game!")
                print()
                print("------------------------------------------------------------")
                print()
                break
            else:
                print("Invalid Input. Try again!")
            
main()
