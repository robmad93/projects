playerOneCards = [10, 6, 8, 9, 7, 12, 7]
playerTwoCards = [7, 6, 9, 5, 2, 8, 11]
roundNumbers = [1, 2, 3, 4, 5, 6, 7]
winCountPlayerOne = 0
winCountPlayerTwo = 0

string = "Card Busters"
title = string.center(32, "*")
print(title)
for i in range(len(roundNumbers)):
    if playerOneCards[i] > playerTwoCards[i]:
        print("Round number", str(roundNumbers[i]), ": Player 1 wins the round, with", str(playerOneCards[i]), "beating", str(playerTwoCards[i]))
        winCountPlayerOne += 1
    elif playerOneCards[i] < playerTwoCards[i]:
        print("Round number", str(roundNumbers[i]), ": Player 2 wins the round, with", str(playerTwoCards[i]), "beating", str(playerOneCards[i]))
        winCountPlayerTwo += 1
    else:
        print("Round number", str(roundNumbers[i]), ": This round has ended in a draw")
if winCountPlayerOne > winCountPlayerTwo:
    print("\nPlayer 1 wins the game, by", str(winCountPlayerOne), "wins to", str(winCountPlayerTwo))
elif winCountPlayerOne < winCountPlayerTwo:
    print("\nPlayer 2 wins the game, by", str(winCountPlayerTwo), "wins to", str(winCountPlayerOne))
else:
    print("\nThe game has ended in a tie!")
