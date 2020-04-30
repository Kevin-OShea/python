import math
import random
import subprocess


board = ['A','A','A','A','A','A','A','A','A']

class play:

    def place_piece(piece, place):
        board[place] = piece
        if(board[place] == piece):
            return true
        return false


    def print_board_data():
        for i in range(len(board)):
            print(' ' + board[i] + ' ', end='')
            if(i != 0 and (i == 2 or i == 5 or i == 8)):
                print('')

    def read_in():
        array = [-1,-1]
        input_data = input("Please enter location of desired placement in the following format: (X,0): ")
        for i in input_data:
            if( i.isnumeric()):
                array[1] = i
            elif(i == 'X' or i == 'O'):
                array[0] = i
        board[int(array[1])] = array[0]
        print(board)



# print_board_data()
play.read_in()
