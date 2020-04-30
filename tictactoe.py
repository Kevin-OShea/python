import math
import random
import subprocess


# board = ['A','A','A','A','A','A','A','A','A']
board = ['X','X','X','A','A','A','A','A','A']

class play:

    def print_board_data():
        for i in range(len(board)):
            print(' ' + board[i] + ' ', end='')
            if(i != 0 and (i == 2 or i == 5 or i == 8)):
                print('')

    def read_in_and_write():
        current_player = 'X'
        array = [-1,-1]
        input_data = input("Please enter location of desired placement in the following format: (X,0): ")
        for i in input_data:
            if( i.isnumeric()):
                array[1] = i
            elif(i == 'X' or i == 'O'):
                array[0] = i
        board[int(array[1])] = array[0]
        play.print_board_data()

    def check_win():
        if(board[4] == board[0] and board[4] == board[8]): # diag top left to right
            print(board[4] + ' WINS!')
        elif(board[4] == board[6] and board[4] == board[2]): # diag bot left to right
            print(board[4] + ' WINS!')
        elif(board[0] == board[1] and board[0] == board[2]): # top left to right
            print(board[0] + ' WINS!')
        elif(board[3] == board[4] and board[5] == board[2]): # middle left to right
            print(board[3] + ' WINS!')
        elif(board[6] == board[7] and board[6] == board[8]): # bot left to right
            print(board[6] + ' WINS!')
        elif(board[0] == board[3] and board[0] == board[6]): # top left down
            print(board[0] + ' WINS!')
        elif(board[1] == board[4] and board[1] == board[7]): # middle down
            print(board[1] + ' WINS!')
        elif(board[2] == board[5] and board[8] == board[2]): # right down
            print(board[2] + ' WINS!')


# print_board_data()
play.check_win()
