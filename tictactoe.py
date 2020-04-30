import math
import random
import subprocess


board = ['A','A','A','A','A','A','A','A','A']
count = 0
class play:

    def print_board_data():
        for i in range(len(board)):
            print(' ' + board[i] + ' ', end='')
            if(i != 0 and (i == 2 or i == 5 or i == 8)):
                print('')

    def read_in_and_write():
        current_player = 'X'
        array = [-1,-1]
        valid = False
        while(valid == False):
            input_data = input("Please enter location of desired placement in the following format: (X,0): ")
            if(len(input_data) != 5):
                print('Please input in correct format')
                continue
            if(input_data[3].isnumeric() and board[int(input_data[3])] == 'A' and int(input_data[3]) > -1 and int(input_data[3]) < 9):
                array[1] = input_data[3]
            else:
                print('Please place piece into a valid space')
                continue

            if(input_data[1] == current_player):
                array[0] = input_data[1]
                count = count + 1
                if(current_player == 'X'):
                    current_player = 'O'
                else:
                    current_player = 'X'
                board[int(array[1])] = array[0]
                play.print_board_data()
                if(play.check_win()):
                    break
                else:
                    continue
            else:
                print('Please place the correct piece')
                continue

    def check_win():
        if(board[4] != 'A' and board[4] == board[0] and board[4] == board[8]): # diag top left to right
            print(board[4] + ' WINS!')
            return True
        elif(board[4] != 'A' and board[4] == board[6] and board[4] == board[2]): # diag bot left to right
            print(board[4] + ' WINS!')
            return True
        elif(board[0] != 'A' and board[0] == board[1] and board[0] == board[2]): # top left to right
            print(board[0] + ' WINS!')
            return True
        elif(board[3] != 'A' and board[3] == board[4] and board[5] == board[2]): # middle left to right
            print(board[3] + ' WINS!')
            return True
        elif(board[6] != 'A' and board[6] == board[7] and board[6] == board[8]): # bot left to right
            print(board[6] + ' WINS!')
            return True
        elif(board[0] != 'A' and board[0] == board[3] and board[0] == board[6]): # top left down
            print(board[0] + ' WINS!')
            return True
        elif(board[1] != 'A' and board[1] == board[4] and board[1] == board[7]): # middle down
            print(board[1] + ' WINS!')
            return True
        elif(board[2] != 'A' and board[2] == board[5] and board[8] == board[2]): # right down
            print(board[2] + ' WINS!')
            return True
        elif(count == 9):
            print('TIE!')
            return True



# print_board_data()
play.read_in_and_write()
