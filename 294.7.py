from random import randrange

def main ():
    printIntro()
    n = getInput()
    wins, losses = simNGames(n)
    printSummary(n, wins)

def printIntro():
    print ("This program simulates multiple games of craps, a dice game played at casinos.")

def getInput():
    n=eval(input("\nPlease enter the number of games that you would like to simulate: " ))
    return n

def rollDice():
    return randrange(1,7) + randrange(1,7)

def simOneGame():
    #Simulates a single craps game
    initial_roll = rollDice()
    outcome = None
    if initial_roll == 7 or initial_roll == 11:
        outcome = "win"
    elif initial_roll == 2 or initial_roll == 3 or initial_roll == 12:
        outcome = "lose"
    else:
        roll = rollDice()
        while roll != 7 and roll != initial_roll:
            roll = rollDice()
        if roll == initial_roll:
            outcome = "win"
        elif roll == 7:
            outcome = "lose"
    return outcome

def simNGames(n):
    #Simulates n games of craps
    wins = 0
    losses = 0
    for i in range(n):
        outcome = simOneGame()
        if outcome == "win":
            wins += 1
        else:
            losses += 1
    return wins, losses

def printSummary(n, wins):
    print ("\nGames simulated:", n)
    print ("Games won:", wins)
    print ("Probability of winning is", wins/n)



if __name__=='__main__':
    main ()
