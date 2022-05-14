import random
import math
import pr1testing
import statistics as stat
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:

        ##player1
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d

            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True

        ##player2
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2):


    player1 = "Player1"
    player2 = "Player2"
    score1 = 0
    score2 = 0
    last = False
    while True:

        ##player1
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = strat1(score1, score2, last) #Instead of having players decide, strategy1 decides for them. It takes the initial 3 inputs: 0,0, False and runs.
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True

        ##player2
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = strat2(score2, score1, last)
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3
#end of autoplayLoud

#enter autoplay (silent)
def autoplay(strat1, strat2):

    score1 = 0
    score2 = 0
    last = False
    while True:

        ##player1

        numDice = strat1(score1, score2, last)
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last: #what's this last is doing?
            break
        if numDice == 0:
            last = True # what does this do?

        ##player2

        numDice = strat2(score2, score1, last)
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True


    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3

def manyGames(strat1, strat2, n): #many games takes strategies and output results over n number of times. cool!

    S1_wins = 0 #initializing conditions
    S2_wins = 0
    ties = 0

    if n%2 == 1:#checking if the number is odd

        results = autoplay(strat1, strat2) #storing the results from autoplay function where player 1 goes first.

        if results == 2: #if odd, then see what's the result update the scores of player and subtract one to make the number even
            S2_wins += 1
            n -=1

        elif results == 1:
            S1_wins += 1
            n -=1

        else:
            ties +=1
            n -=1

#now since we are at evens, half the time make player one goes first, half the time player2 goes first
    i = 0
    while i <= n/2:
        results = autoplay(strat1, strat2)
        i += 1

        if results == 2:
            S2_wins += 1

        elif results == 1:
            S1_wins += 1 #updating the results accordingly

        else:
            ties +=1



    i = 0
    while i <= n/2:
        results = autoplay(strat2, strat1)
        i += 1

        if results == 2:
            S1_wins += 1

        elif results == 1:
            S2_wins += 1

        else:
            ties +=1

    print("Player 1 wins : " + str(S1_wins))
    print("Player 2 wins : " + str(S2_wins))
    print("Ties : " + str(ties))

#end of many games



def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
        return 12

def sample2(myscore, theirscore, last):

    if myscore <= 50:
        return 30
    elif myscore >=51 and myscore < 80:
        return 10
    else:
        return 0



def improve(strat):

    def new_strat(myscore, theirscore, last):
        if myscore >= 100:
            return 0
        else:
            return strat(myscore, theirscore, last)

    return new_strat


def myStrategy(myscore, theirscore, last):

    diff = myscore-theirscore
    theirdist = 100 - theirscore
    mydist = 100 - myscore


    if theirscore == 0:
        return 33


    elif theirdist < mydist:
        return (theirscore-myscore)//2.5 + 1


    else:
        return (mydist)//4
