from random import randrange

def main ():
    printIntro()
    n=getInput()
    wins, losses=simNGames(n)
    printSummary(n, wins)

def printIntro():
    print ("This program simulates multiple games of craps, a dice game played at casinos.")

def getInput():
    n=eval(input("\nPlease enter the number of games that you would like to simulate. " ))
    return n

def simOneGame():
    #Simulates a single craps game
    initialroll=randrange(1,13)
    outcome=None
    if initialroll==7 or initialroll==11:
        outcome="win"
    elif initialroll==2 or initialroll==3 or initialroll==12:
        outcome="lose"
    else:
        roll=randrange(1,13)
        while roll!=7 and roll!=initialroll:
            roll=randrange(1,13)
        if roll==initialroll:
            outcome="win"
        if roll==7:
            outcome="lose"
    return outcome

def simNGames(n):
    #Simulates n games of craps
    wins=0
    losses=0
    for i in range(n):
        outcome=simOneGame()
        if outcome=="win":
            wins+=1
        else:
            losses+=1
    return wins, losses

def printSummary(n, wins):
    print ("\nGames simulated:", n)
    print ("Games won:", wins)
    print ("Probability of winning is", wins/n)



if __name__=='__main__':
    main ()
