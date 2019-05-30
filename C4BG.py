

import connectfour


def print_board(gamestate)->None:
    '''prints the board with the current gamestate'''
    print('-------------------')
    print('1  2  3  4  5  6  7')
    for rows in range(connectfour.BOARD_ROWS):
        for columns in range(connectfour.BOARD_COLUMNS):
            if gamestate.board[columns][rows] == connectfour.NONE:
                print('.', end = '  ')
            elif gamestate.board[columns][rows] == connectfour.RED:
                print('R', end = '  ')
            elif gamestate.board[columns][rows] == connectfour.YELLOW:
                print('Y', end = '  ')
        print()

        

def userinput():
    '''requests user input for pop/drop and column number'''
    while True:
        userinput = input("Enter (Pop or Drop) and a Column Number (1-7): ")
        popdrop = userinput.split()[0]
        colnumb = userinput.split()[1]
        if popdrop not in ('POP','DROP','drop','pop','Drop','Pop'):
            print("Please enter valid format (POP/pop, DROP/drop)")
            continue
        else:
            break
    return popdrop.upper(), colnumb.upper()




def change_board(gamestate:object,user_input,column_number):
    '''changes the board and updates the gamestate according to the users action'''
    if user_input == 'DROP':
        gamestate = connectfour.drop(gamestate, (int(column_number)-1))
    if user_input == 'POP':
        gamestate = connectfour.pop(gamestate, (int(column_number)-1))
    print_board(gamestate)
    return( gamestate )
    

def det_winner(gamestate):
    '''checks for a winner and returns the winner with its according color, breaks out of program'''
    if connectfour.winner(gamestate) != 0:
        if gamestate.turn == 2:
            print("RED IS THE WINNER!")
        elif gamestate.turn == 1:
            print("YELLOW IS THE WINNER!")
        return False

