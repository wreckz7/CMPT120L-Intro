#Functions.py
#This program will use the 5-question quiz from the Chapter 7 assignment, and restructure the code to employ three functions (since there are hints): askQuestion(), askHint() and printFinalScore()
#by Awais Razaque 10/31/23

def askQuestion(question, choices, answer):
    global questionnumber
    global hintornot
    print(question)
    print(choices)
    hint = input("Do you want a hint before answering? You cannot get a hint after you answer and you will get half a point! Please type (y/n): ").lower()
    if hint == "y":
        askHint(questionnumber)
        hintornot = True
    elif hint == "n":
        print("You have chosen no hint for this question!")
        hintornot = False
    else:
        print("Invalid Choice!")
    print()
    correctstatements = ["Max Verstappen is our 2023 F1 World Champion!", "Lewis Hamilton and Michael Schumacher are both tied with seven titles apiece!", "Fernando Alonso has 375 total entries into a race!", "Lewis Hamilton has the most wins alone with 103 wins in his ongoing career!", "Ferrari has the most wins with 243!"]
    useranswer = input("What is your choice? ").lower()
    if useranswer == answer:
        print("That is correct, " + correctstatements[questionnumber])
        print("________________________________________________________________________________")
        print()
        return True
    else:
        print("Sorry that is incorrect!")
        return False

def askHint(questionnum):
    hint = ["This driver drives for Red Bull/Honda RBPT.", "Your choices are now:\na) Four\nb) Two", "This driver is still racing and is racing for Aston Martin.", "This driver is still racing and is racing for Mercedes.", "This team is an Italian beacon in the world."]
    print(hint[questionnum])

def printFinalScore(finalscore):
    if finalscore >= 0 and finalscore <= 2: #Score being 0, 0.5, 1, 1.5 or 2 then do this
        print("Better luck next time. You scored a:", finalscore)
    elif finalscore >= 2.5 and finalscore <= 4: #Score being 2.5, 3, 3.5, or 4 then do this
        print("Not bad. Try again soon! You scored a:", finalscore)
    else: #Score being 4.5 or 5
        print("Awesome! You rock! You scored a:", finalscore)

def main():
    #intro
    print("Welcome to this program!")
    print("This program will use the 5-question quiz from the Chapter 7 assignment, and restructure the code to employ three functions (since there are hints): askQuestion(), askHint() and printFinalScore()")
    print()
    print("Chapter 7 Assignment Intro:\nThis program will ask five questions and keep score of the number of correct answers that you enter, and then display your score at the end of the program.")
    print("The topic of this quiz will be Formula One and will be all multiple choice, where you enter a, b, c, etc.\nThe program will also ask you if you want a hint, but this will mean you get half a point instead of 1 onto your score!")
    print()
    print("Goodluck and have fun!")
    input ("Press <Enter> to start this quiz!")
    print("________________________________________________________________________________")
    print()
    question = ["Q1: Who is the 2023 Formula One World Drivers' Champion? This driver was crowned the Champion after placing second in the 2023 F1 Qatar GP Sprint on October 7th, 2023.", "Q2: How many drivers are tied for the most Formula One World Drivers' Championships?", "Q3: Who has raced the most Formula One races in their career?", "Q4: Who has the most total wins in their career?", "Q5: What team has won the most Formula One Grand Prix Races?"]
    choices = ["a) Lewis Hamilton\nb) Lando Norris\nc) Max Verstappen\nd) Fernando Alonso", "a) Four\nb) Two\nc) One", "a) Fernando Alonso\nb) Lewis Hamilton\nc) Rubens Barrichelo\nd) Kimi Räikkönen", "a) Michael Schumacher\nb) Lewis Hamilton\nc) Ayrton Senna", "a) Williams\nb) McLaren\nc) Mercedes\nd) Ferrari"]
    answer = ["c", "b", "a", "b", "d"]
    global questionnumber
    global score
    global hintornot
    score = 0
    for i in range (len(question)):
        questionnumber = i
        if askQuestion(question[i], choices[i], answer[i]) == True:
            if hintornot == False:
                score = score + 1
            elif hintornot == True:
                score = score + 0.5
        else:
            print("Your score was not incremented.")
            print("________________________________________________________________________________")
            print()
    printFinalScore(score)
    print()
    print("Thank you for playing this quiz!")
    input ("Press <Enter> to end this program!")

main()
