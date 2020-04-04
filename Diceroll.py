import random

def main():
    Player1 = 0
    Player1wins = 0
    Player2 = 0
    Player2wins = 0
    rounds = 1

    while rounds != 10:
        print("Round " + str(rounds))
        Player1 = dice_roll()
        Player2 = dice_roll()
        print("Player 1 Roll:" + str(Player1))
        print("Player 2 Roll:" + str(Player2))

        if Player1 == Player2:
            print("DRAW!")
        elif Player1 > Player2:
            Player1wins = Player1wins + 1
            print("Player 1 wins!")
        else:
            Player2wins = Player2wins + 1
            print("Player 2 wins!")

        rounds = rounds + 1

    if Player1wins == Player2wins:
        print("OVERALL DRAW!")
    elif Player1wins > Player2wins:
        print("Player 1 Wins! Rounds Won: " + str(Player1wins))
    else:
        print("Player 2 Wins! Rounds Won: " + str(Player2wins))

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()