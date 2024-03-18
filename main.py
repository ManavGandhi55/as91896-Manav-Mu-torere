'''Mū tōrere is a Moari board game played on an octagon shaped board, which has 9 spots 
to place the stones on, one on each corner of the octagon called periperi and lines 
connecting it to the center which is called the Putahi, which is the 9th spot. In order 
to win you have to try and block the opposing player from being able to make a name'''

spots = {
    1: "B",
    2: "B",
    3: "B",
    4: "B",
    5: "R",
    6: "R",
    7: "R",
    8: "R",
    9: "0"
}
# The dictionary above stores the starting positions of the stones on the board.

player1 = "B"
player2 = "R"
secspots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#This list stores the spots that are available to be played on.


def mainboard():
    print('\n    ' + spots[8] + '8  --  ' + spots[1] + '1   ')
    print('   \\          /')
    print('  ' + spots[7] + '7          ' + spots[2] + '2')
    print('  --    ' + spots[9] + '9    --')
    print('  ' + spots[6] + '6          ' + spots[3] + '3   ')
    print('   /          \\')
    print('    ' + spots[5] + '5  --  ' + spots[4] + '4   ')
#This function prints the main board.

def secondboard():
    print('\n     ' + secspots[7] + '  -  ' + secspots[0] + '   ')
    print('    \\       /')
    print('   ' + secspots[6] + '         ' + secspots[1] + '')
    print('   -    ' + secspots[8] + '    -')
    print('   ' + secspots[5] + '         ' + secspots[2] + '   ')
    print('    /       \\')
    print('     ' + secspots[4] + '  -  ' + secspots[3] + '   ')
#This function prints the second board which holds the spots that are available.

mainboard()
#prints main board
secondboard()
#prints second board
print("Welcome to my Mū tōrere game, made my Manav Gandhi")

namelist = []
player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")
namelist.append(player1)
namelist.append(player2)
#This is a part of code which asks the players for their playernames
#modifies namelist to include the names of the players.
if len(namelist) == 2:
    print("Welcome", namelist[0], "and", namelist[1],
          "to the traditional Maori game, Mū tōrere!")
    #This introduces the game to the players, including their playername variables
else:
    print("Please enter a valid name for player 1 and 2")
    #This if else statement checks if there are 2 player names inputted into the code.
    #and if not, it asks the user to enter a valid name for player 1 and 2.
rulescheck = input("Do you know the rules of Mu torere: ").lower()
if rulescheck == "yes":
    print("Okay lets get started then...")
else:
    print("The rules to Mu torere are very simple...")
    print("The game is played on an 8-sided board, with 9 spots to place the stones on  as the spot in the middle (the putahi) is the 9th spot. Each player takes turns moving to an unoccupied spot on the board. Two players cannot occupy the same spot at the same time. In order to win, you need to block the opposing player from being able to move.")
    


playermoves = []

#This list stores the moves of the players.

    
    