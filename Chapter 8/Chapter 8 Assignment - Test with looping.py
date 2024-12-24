#Test with looping.py
#This program will modify the Chapter 7 assignment to continue asking the same quiz question until the user guesses the correct answer or types 'skip'.
#If the user guesses correctly, the program will say 'correct', otherwise an incorrect message will print 'sorry, try again' and when 'skip' is typed by the user, the program will print the correct answer and move on.
#The user will also be notified of their attempts per question and be given a warning to perhaps skip when they have answered the current question twice.
#At the end of the program the user can choose to play again or not and the program will also give the user their average attempts over all 5 questions, as each question in the quiz will be multiple choice with 4 answer choices.
#by Awais Razaque 10/17/23

def main():
    loopornot = True
    while loopornot == True:
        print("Welcome to this program!")
        print("This program will modify the Chapter 7 assignment to continue asking the same quiz question until the user guesses the correct answer or types 'skip'.")
        print("If the user guesses correctly, the program will say 'correct', otherwise an incorrect message will print 'sorry, try again' and when 'skip' is typed by the user, the program will print the correct answer and move on.")
        print("The user will also be notified of their attempts per question and be given a warning to perhaps skip when they have answered the current question twice.")
        print("At the end of the program the user can choose to play again or not and the program will also give the user their average attempts over all 5 questions, as each question in the quiz will be multiple choice with 4 answer choices.")
        print()
        print("The topic of this quiz will be Formula One and this time there will be no hints.\nGoodluck and have fun!")
        print()

        #initial statements
        question1 = question2 = question3 = question4 = question5 = False
        skip1 = skip2 = skip3 = skip4 = skip5 = False

        count1 = 0
        while question1 == False:
            print("Q1: Who is the 2023 Formula One World Drivers' Champion? This driver was crowned the Champion after placing second in the 2023 F1 Qatar GP Sprint on October 7th, 2023.")
            print("a) Lewis Hamilton\nb) Lando Norris\nc) Max Verstappen\nd) Fernando Alonso")
            print()
            answer1 = input("What is your choice? ").lower()
            count1 = count1 + 1
            if answer1 == "c":
                print("That is correct, Max Verstappen is our 2023 F1 World Champion! Moving onto the next question...")
                print("It took you", count1, "time(s) to answer this question correctly!")
                question1 = True
            elif answer1 == "skip":
                print("The correct answer was Max Verstappen! Moving onto the next question...")
                print("You attempted this question", count1 - 1, "time(s) before skipping...")
                skip1 = True
                question1 = True
            elif count1 == 2 and question1 == False:
                print("You have now attempted this question 2 times and still have not got it right. Please consider skipping the question by typing 'skip'")
                print()
            else:
                print()
                print("Sorry, try again!")
                print("You have attempted this question", count1, "time(s)!")
                print()
        print("________________________________________________________________________________")
        print()

        count2 = 0
        while question2 == False:
            print("Q2: How many drivers are tied for the most Formula One World Drivers' Championships?")
            print("a) Four\nb) Two\nc) One\nd) Three")
            print()
            answer2 = input("What is your choice? ").lower()
            count2 = count2 + 1
            if answer2 == "b":
                print("That is correct, Lewis Hamilton and Michael Schumacher are both tied with seven titles apiece!")
                print("It took you", count2, "time(s) to answer this question correctly!")
                question2 = True
            elif answer2 == "skip":
                print("The correct answer was Two! Moving onto the next question...")
                print("You attempted this question", count2 - 1, "time(s) before skipping...")
                skip2 = True
                question2 = True
            elif count2 == 2 and question2 == False:
                print("You have now attempted this question 2 times and still have not got it right. Please consider skipping the question by typing 'skip'")
                print()
            else:
                print()
                print("Sorry, try again!")
                print("You have attempted this question", count2, "time(s)!")
                print()
        print("________________________________________________________________________________")
        print()

        count3 = 0
        while question3 == False:
            print("Q3: Who has raced the most Formula One races in their career?")
            print("a) Fernando Alonso\nb) Lewis Hamilton\nc) Rubens Barrichelo\nd) Kimi Räikkönen")
            print()
            answer3 = input("What is your choice? ").lower()
            count3 = count3 + 1
            if answer3 == "a":
                print("That is correct, Fernando Alonso has 375 total entries into a race!")
                print("It took you", count3, "time(s) to answer this question correctly!")
                question3 = True
            elif answer3 == "skip":
                print("The correct answer was Fernando Alonso! Moving onto the next question...")
                print("You attempted this question", count3 - 1, "time(s) before skipping...")
                skip3 = True
                question3 = True
            elif count3 == 2 and question3 == False:
                print("You have now attempted this question 2 times and still have not got it right. Please consider skipping the question by typing 'skip'")
                print()
            else:
                print()
                print("Sorry, try again!")
                print("You have attempted this question", count3, "time(s)!")
                print()
        print("________________________________________________________________________________")
        print()

        count4 = 0
        while question4 == False:
            print("Q4: Who has the most toal wins in their career?")
            print("a) Michael Schumacher\nb) Lewis Hamilton\nc) Ayrton Senna\nd) Max Verstappen")
            print()
            answer4 = input("What is your choice? ").lower()
            count4 = count4 + 1
            if answer4 == "b":
                print("That is correct, Lewis Hamilton has the most wins alone with 103 wins in his ongoing career!")
                print("It took you", count4, "time(s) to answer this question correctly!")
                question4 = True
            elif answer4 == "skip":
                print("The correct answer was Lewis Hamilton! Moving onto the next question...")
                print("You attempted this question", count4 - 1, "time(s) before skipping...")
                skip4 = True
                question4 = True
            elif count4 == 2 and question4 == False:
                print("You have now attempted this question 2 times and still have not got it right. Please consider skipping the question by typing 'skip'")
                print()
            else:
                print()
                print("Sorry, try again!")
                print("You have attempted this question", count4, "time(s)!")
                print()
        print("________________________________________________________________________________")
        print()

        count5 = 0
        while question5 == False:
            print("Q5: What team has won the most Formula One Grand Prix Races?")
            print("a) Williams\nb) McLaren\nc) Mercedes\nd) Ferrari")
            print()
            answer5 = input("What is your choice? ").lower()
            count5 = count5 + 1
            if answer5 == "d":
                print("That is correct, Ferrari has the most wins with 243!")
                print("It took you", count5, "time(s) to answer this question correctly!")
                question5 = True
            elif answer5 == "skip":
                print("The correct answer was Ferrari! Moving onto the next question...")
                print("You attempted this question", count5 - 1, "time(s) before skipping...")
                skip5 = True
                question5 = True
            elif count5 == 2 and question5 == False:
                print("You have now attempted this question 2 times and still have not got it right. Please consider skipping the question by typing 'skip'")
                print()
            else:
                print()
                print("Sorry, try again!")
                print("You have attempted this question", count5, "time(s)!")
                print()
        print("________________________________________________________________________________")
        print()

        if skip1 == skip2 == skip3 == skip4 == skip5 == True:
            averageattempts = 0
            print("The quiz has been finished! Your average attempts over all 5 questions was: ", averageattempts)
            print("This means you skipped every question!")
        else:
            averageattempts = (count1 + count2 + count3 + count4 + count5)/ 5
            print("The quiz has been finished! Your average attempts over all 5 questions was: ", averageattempts)
        againloop = input("Do you want to play again? If yes, please type y or if no, type n: ").lower()
        if againloop == "n":
            loopornot = False
            print("Thank you for playing this quiz!")
            input ("Press <Enter> to end this program!")
        else:
            print("________________________________________________________________________________")
            print()
        
main()
