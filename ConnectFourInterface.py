# Kenny Matsudo 28917382 and Claudia Cota 60341850

import connectfour
import C4BG


def run(gamestate):
    '''runs console game in a while loop'''
    game_running = True
    print("Welcome to ConnectFour!")
    C4BG.print_board(gamestate)
    while game_running:
        
        try:
            if gamestate.turn == 1:
                print("Turn: Red")
            elif gamestate.turn == 2:
                print("Turn: Yellow")
            user_input, colnumb = C4BG.userinput()
            print()
            gamestate = C4BG.change_board(gamestate,user_input,colnumb)
            if C4BG.det_winner(gamestate) == False:
                game_running = False
        except:
            print('Invalid User Input')
    


if __name__ == "__main__":
    gamestate = connectfour.new_game()
    run(gamestate)
