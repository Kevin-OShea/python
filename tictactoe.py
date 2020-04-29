import math
import random
import subprocess
import sys

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
        a = input("Please enter location of desired placement in the following format: (0,0): ")
        print(a)


# print_board_data()
play.read_in()
