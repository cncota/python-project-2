# Kenny Matsudo 28917382 and Claudia Cota 60341850

import serverlogic
import C4BG
import connectfour
import ConnectFourInterface


def run():
    '''runs game against the server using hidden functions'''
    
    try:
        host = input('Enter host: ')
        port = input('Enter port: ')
        connected = serverlogic.connect(host,int(port))
        game_state = connectfour.new_game()
        username = serverlogic.get_username()
        serverlogic.login(connected,username)
        serverlogic.send(connected)

    except:
        print("--Invalid Input--")



    else:

        while connectfour.winner(game_state) == connectfour.NONE:
            
            try:
                print()
                print("Turn:RED")
                print()
                popdrop, column_number = C4BG.userinput()
                print()
                game_state = C4BG.change_board(game_state,popdrop,column_number)
            except:
                print("Please re-enter")
            
            else:
                print('-------------------')
                print()
                print("Yellow's turn")
                print()
                print("Server Response:")
                to_server = popdrop.upper() + ' ' + str(column_number)
                serv_response = serverlogic.server_popdrop(connected,to_server)
                print()
                if serv_response == 'WINNER_RED':
                    serverlogic.closeconnection(connected)
                    break
                if serv_response == 'WINNER_YELLOW':
                    serverlogic.closeconnection(connected)
                    break
                if serv_response != 'READY':
                    server_drop = serv_response.split()[0]
                    server_column = serv_response.split()[1]
                    game_state = C4BG.change_board(game_state,server_drop,server_column)



if __name__ == '__main__':
    run()
