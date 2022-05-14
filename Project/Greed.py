#randomize the process

import random as rd

player1 = 0
player2 = 0

def play(k,m):

    dice_list1 = []
    dice_list2 = []

    for i in range (0,k):
        n = rd.randint(0,5)

        dice_list1.append(n)

    sum_1 = sum(dice_list1)



    for j in range (0,m):
        n = rd.randint(0,5)

        dice_list2.append(n)


    sum_2 = sum(dice_list2)

    scores = [sum_1, sum_2]

    return scores




while player1 < 100 and player2 < 100:

    k = int(input("Player 1, how many dice:"))
    m = int(input("Player 2, how many dice:"))

    if k !=0 and m !=0:


        scores = play(k,m)

        player1 = player1 + scores[0]
        print(player1)
        player2 = player2 + scores[1]
        print(player2)

    elif k==0:
        print("Player2 wins!")

    else:
        print("Player1 wins!")


if player1 >= 100:

    print("Player2 wins!")

elif player2 >=100:

    print("Player1 wins!")

else:

    print("Warning,league end without a winner")
