import random
class DiceGame:
    
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.score = 0

    def rollDice(self):
        self.score = 0
        for i in range(self.num_dice):
            roll = random.randint(1,6)
            print("You rolled a", roll, "on roll", i+1)
            self.score = self.score + roll
        return self.score
    
    def getScore(self):
        return self.score
    
def main():
    player1_score = 0
    player2_score = 0
    player1 = DiceGame(4)
    player2 = DiceGame(4)
 
    
    # call the rollDice() for player 1. Print out the returned score.
    print("Player 1 rolls first:")
    player1.rollDice()
    player1_score = player1.getScore()
    print("Player 1's score is:",player1_score)

    #Repeat the same for Player 2
    print("Player 2 rolls first:")
    player2.rollDice()
    player2_score = player2.getScore()
    print("Player 2's score is:",player2_score)

    #Check for winner:
    #if player 1's score is greater than player 2's score:
    if player1_score > player2_score:
        print("Player 1 wins this round")

    #else if player 2's score is greater than player 1's score:
    elif player2_score > player1_score:
        print("Player 2 wins this round")

    #else a tie occurred
    else:
        print("This round was a tie.")

main()

