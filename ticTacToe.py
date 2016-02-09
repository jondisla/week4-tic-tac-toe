theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

    
        print (board['top-L'],'|', board['top-M'],'|',board['top-R'])
        print ('--|---|--')
        print (board['mid-L'],'|', board['mid-M'],'|',board['mid-R'])
        print ('--|---|--')
        print (board['low-L'],'|', board['low-M'],'|',board['low-R'])
    
printBoard(theBoard)
    
def checkWinner(board, player):
    print('Checking if ' + player + ' is a winner...')
    return((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player)#top row
        or (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player)#middle row
        or (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player)#bottom row
        or (board['low-L'] == player and board['mid-M'] == player and board['top-R'] == player)#cross
        or (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player)#cross
        or (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player)#left 
        or (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player)#right
        or (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player))#middle
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################

    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #creates new value assigned to turn
    for i in range(9): #the range here is 9 for every square on the board
        printBoard(board)#prints the board on the screen
        print('Turn for ' + turn + '. Move on which space?')
        ##prints the intstructions and uses the 'turn' for the letter
        move = input()   #gets the keyboard input
        board[move] = turn
        if( checkWinner(board, 'X') ):
            #loop to continously check on the checkwinner function
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):
            #prints 'o' if the condition of checkwinner is met
            print('O wins!')
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
