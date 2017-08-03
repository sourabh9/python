#!/usr/bin/python

####Method 1
player1 = raw_input("Enter your name, please :")
player2 = raw_input("Enter your name, please :")
# choice = ['Rock','scissors','paper']


def rules(choice1, choice2) :
    if (choice1 == 'Rock') & (choice2 == 'scissors'):
        print "winner is:" + player1
    if (choice1 == 'scissors') & (choice2 == 'Rock'):
        print "winner is:" + player2
    if (choice1 == 'paper') & (choice2 == 'scissors'):
        print "winner is:" + player2
    if (choice1 == 'scissors') & (choice2 == 'paper'):
        print "winner is:" + player1
    if (choice1 == 'Rock') & (choice2 == 'paper'):
        print "winner is:" + player2
    if (choice1 == 'paper') & (choice2 == 'Rock'):
        print "winner is:" + player1
    # else :
    #     print "Wrong choice is made, please play again.."

while True:
    print "Do you want to play the game ?"
    input_cmd = raw_input()
    if input_cmd == "yes":
        print "Let us play..."
        c1 = raw_input("first player, what is your choice: ")
        c2 = raw_input("second player, what is your choice: ")
        rules(c1, c2)
    else:
        print "Exiting from the Game...Thanks.."
        break