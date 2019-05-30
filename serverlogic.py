# Kenny Matsudo 28917382 and Claudia Cota 60341850

from collections import namedtuple
import socket

GameConnection = namedtuple('GameConnection',['socket','gameinput','gameoutput'])

class GameError(Exception):
    pass

def connect(host:str,port:int)-> GameConnection:
    '''makes connection with a server, with the given host and port'''
    game_socket = socket.socket()
    game_socket.connect((host,port))

    game_input = game_socket.makefile('r')
    game_output = game_socket.makefile('w')

    return GameConnection(
        socket = game_socket,
        gameinput = game_input,
        gameoutput = game_output)



def login(connection:GameConnection, username: str) -> None:
    '''sends protocol to server with the given username'''
    _write_line(connection, 'I32CFSP_HELLO' + ' ' + username)
    return _expect_line(connection, 'WELCOME' + ' ' + username)


def send(connection:GameConnection):
    '''sends game starting protocol to server'''
    _write_line(connection, 'AI_GAME')
    return _expect_line(connection, 'READY')


def server_popdrop(connection:GameConnection, console_input: str):
    '''handles server's response'''

    _write_line(connection,console_input)
    serv_check = connection.gameinput.readline()[:-1]
    
    if serv_check == 'WINNER_RED':
        return serv_check
    server_response = connection.gameinput.readline()[:-1]
    print(server_response)
    if server_response =='READY':
        return server_response
    server_ready = connection.gameinput.readline()[:-1]
    print(server_ready)
    return server_response 


def closeconnection(connection: GameConnection):
    'Closes socket connection'
    connection.gameinput.close()
    connection.gameoutput.close()
    connection.socket.close()


def get_username():
    '''asks user for a username with the given perameters'''
    name = input('Enter a username: ')
    if (' ' in name) == True:
        print('--Enter a valid username--')
    else:
        return name


def _write_line(connection: GameConnection, message: str) -> None:
    '''writes message to the server'''
    connection.gameoutput.write(message + '\r\n')
    connection.gameoutput.flush()


def _expect_line(connection: GameConnection, expected: str) ->str:
    '''checks for expected server response and prints it'''
    line = connection.gameinput.readline()[:-1]

    if line != expected:
        raise GameError()
    else:
        print(line)
    


