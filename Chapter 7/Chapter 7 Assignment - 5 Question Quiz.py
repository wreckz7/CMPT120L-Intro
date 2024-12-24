#5 Question Quiz.py
#This program will ask five questions and keep score of the number of correct answers that the user enters, and then display there score at the end of the program.
#by Awais Razaque 10/10/23

def main():
    #intro
    print("Welcome to this program!")
    print("This program will ask five questions and keep score of the number of correct answers that you enter, and then display your score at the end of the program.")
    print()
    print("The topic of this quiz will be Formula One and will be all multiple choice, where you enter a, b, c, etc.\nThe program will also ask you if you want a hint, but this will mean you get half a point instead of 1 onto your score!")
    print()
    print("Goodluck and have fun!")
    print()
    #initial statements
    score = 0
    hintvalv1 = False
    hintvalv2 = False
    hintvalv3 = False
    hintvalv4 = False
    hintvalv5 = False

    #question 1
    print("Q1: Who is the 2023 Formula One World Drivers' Champion? This driver was crowned the Champion after placing second in the 2023 F1 Qatar GP Sprint on October 7th, 2023.")
    print("a) Lewis Hamilton\nb) Lando Norris\nc) Max Verstappen\nd) Fernando Alonso")
    print()
    hint1 = input("Do you want a hint before answering? For all hints for any question on this quiz, you cannot get a hint after you answer and you will get half a point! Please type (y/n): ").lower()
    if hint1 == "y":
        hintvalv1 = True
        print("This driver drives for Red Bull/Honda RBPT.")
        print()
    answer1 = input("What is your choice? ").lower()
    if answer1 == "c" and hintvalv1 == True:
        score = score + 0.5
        print("That is correct, Max Verstappen is our 2023 F1 World Champion!\nYour score is now:", score)
    elif answer1 == "c" and hintvalv1 == False:
        score = score + 1
        print("That is correct, Max Verstappen is our 2023 F1 World Champion!\nYour score is now:", score)
    else:
        print("Sorry that is incorrect, you score is:", score)
    print()

    #question 2
    print("Q2: How many drivers are tied for the most Formula One World Drivers' Championships?")
    print("a) Four\nb) Two\nc) One")
    print()
    hint2 = input("Do you want a hint before answering? Please type (y/n): ").lower()
    if hint2 == "y":
        hintvalv2 = True
        print("Your choices are now:\na) Four\nb) Two")
        print()
    answer2 = input("What is your choice? ").lower()
    if answer2 == "b" and hintvalv2 == True:
        score = score + 0.5
        print("That is correct, Lewis Hamilton and Michael Schumacher are both tied with seven titles apiece!\nYour score is now:", score)
    elif answer2 == "b" and hintvalv2 == False:
        score = score + 1
        print("That is correct, Lewis Hamilton and Michael Schumacher are both tied with seven titles apiece!\nYour score is now:", score)
    else:
        print("Sorry that is incorrect, you score is:", score)
    print()

    #question 3
    print("Q3: Who has raced the most Formula One races in their career?")
    print("a) Fernando Alonso\nb) Lewis Hamilton\nc) Rubens Barrichelo\nd) Kimi Räikkönen")
    print()
    hint3 = input("Do you want a hint before answering? Please type (y/n): ").lower()
    if hint3 == "y":
        hintvalv3 = True
        print("This driver is still racing and is racing for Aston Martin.")
        print()
    answer3 = input("What is your choice? ").lower()
    if answer3 == "a" and hintvalv3 == True:
        score = score + 0.5
        print("That is correct, Fernando Alonso has 375 total entries into a race!\nYour score is now:", score)
    elif answer3 == "a" and hintvalv3 == False:
        score = score + 1
        print("That is correct, Fernando Alonso has 375 total entries into a race!\nYour score is now:", score)
    else:
        print("Sorry that is incorrect, you score is:", score)
    print()

    #question 4
    print("Q4: Who has the most total wins in their career?")
    print("a) Michael Schumacher\nb) Lewis Hamilton\nc) Ayrton Senna")
    print()
    hint4 = input("Do you want a hint before answering? Please type (y/n): ").lower()
    if hint4 == "y":
        hintvalv4 = True
        print("This driver is still racing and is racing for Mercedes.")
        print()
    answer4 = input("What is your choice? ").lower()
    if answer4 == "b" and hintvalv4 == True:
        score = score + 0.5
        print("That is correct, Lewis Hamilton has the most wins alone with 103 wins in his ongoing career!\nYour score is now:", score)
    elif answer4 == "b" and hintvalv4 == False:
        score = score + 1
        print("That is correct, Lewis Hamilton has the most wins alone with 103 wins in his ongoing career!\nYour score is now:", score)
    else:
        print("Sorry that is incorrect, you score is:", score)
    print()

    #question5
    print("Q5: What team has won the most Formula One Grand Prix Races?")
    print("a) Williams\nb) McLaren\nc) Mercedes\nd) Ferrari")
    print()
    hint5 = input("Do you want a hint before answering? Please type (y/n): ").lower()
    if hint5 == "y":
        hintvalv5 = True
        print("This team is an Italian beacon in the world.")
        print()
    answer5 = input("What is your choice? ").lower()
    if answer5 == "d" and hintvalv5 == True:
        score = score + 0.5
        print("That is correct, Ferrari has the most wins with 243!\nYour score is now:", score)
    elif answer5 == "d" and hintvalv5 == False:
        score = score + 1
        print("That is correct, Ferrari has the most wins with 243!\nYour score is now:", score)
    else:
        print("Sorry that is incorrect, you score is:", score)
    print()

    #ending
    print("Congratulations you have completed this Formula One Quiz!\nYour results are...")
    print()
    if score >= 0 and score <= 2: #Score being 0, 0.5, 1, 1.5 or 2 then do this
        print("Better luck next time. You scored a:", score)
    elif score >= 2.5 and score <= 4: #Score being 2.5, 3, 3.5, or 4 then do this
        print("Not bad. Try again soon! You scored a:", score)
    else: #Score being 4.5 or 5
        print("Awesome! You rock! You scored a:", score)
    print()
    print("Thank you for playing this quiz!")
    input ("Press <Enter> to end this program!")
  
main()
