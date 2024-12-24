#Object Oriented Lab Original.py
#This program will go through the Object Oriented Programming Lab.
#by Awais Razaque 12/5/23

import random
def main():
    player1_score = 0
    player2_score = 0

    #Start the game

    #call the rollDice() for player 1. Print out the returned score.
    print("Player 1 rolls first: ")
    player1_dice1 = random.randint(1,6)
    player1_dice2 = random.randint(1,6)
    player1_score = player1_dice1 + player1_dice2
    print("Player 1 rolled a: ", player1_dice1)
    print("Player 1 rolled a: ", player1_dice2)

    #Repeat the same for Player 2
    print("Player 2 rolls next: ")
    player2_dice1 = random.randint(1,6)
    player2_dice2 = random.randint(1,6)
    player2_score = player2_dice1 + player2_dice2
    print("Player 2 rolled a: ", player2_dice1)
    print("Player 2 rolled a: ", player2_dice2)  

    #Check for winner:
    #if player 1's score is greater than player 2's score:
    if player1_score > player2_score:
        print("PLayer 1 wins this round!")

    #else if player 2's score is greater than player 1's score:
    elif player2_score > player1_score:
            print("Player 2 wins this round!")

    #else a tie occured
    else:
            print("This round was a tie.")

    print("Thanks for playing this game!")
    input("Press <Enter> to quit this program!")

main()
