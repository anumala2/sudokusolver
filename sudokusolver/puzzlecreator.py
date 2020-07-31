import numpy as np
import pandas as pd
import random

def valid_insert_size6(num, board, i, j):
    if i==0:
        if j==0:
            return True
    for col in range(0, j):
        if board[i][col] == num:
            return False
    print("passcol")
    print(board)
    for row in range(0, i):
        if board[row][j] == num:
            print(row, num)
            return False
    #print("passmain")
    startbox = [int(i/2)*2, int(j/3)*3]
    print(startbox)
    print(board)
    for row in range(startbox[0], startbox[0]+2):
        for col in range(startbox[1], startbox[1]+3):
            if board[row][col] == num:
                return False
    return True

#build a finished puzzle as a numpy 2d array
def create_finished_puzzle(SIZE):
    board = np.zeros((SIZE,SIZE), dtype=int)
    random.seed(1)
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            filled = False
            while not filled:
                temp = random.randint(1, SIZE)
                print(temp, i, j)
                if SIZE==6:
                    if valid_insert_size6(temp, board, i, j):
                        board[i][j] = temp
                        filled = True
    print(board)

def create_finished_puzzle_recurse():
    #trying to make a recursive implementation of board creation

create_finished_puzzle(6)