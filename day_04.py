#!/usr/bin/python

# Advent of Code 2021

# day 04 squid Bingo 

import math


#note: 
# test data has 3 boards defined and 27 call values
# input data has 100 boards defined and 100 call values

# read in the data 
# first line are the calls (load into a single list)
# subsequent data is a blank, followed by 5 rows of 5 values representing a board
# Each position in the board will be a tuple: number and called flag



def readCalls(line):
    print("Reading calls...")
    values = line.split(',')
    calls = []
    for v in values:
        print("v=%s" % v)
        if v != '':
            calls.append(int(v))

    print("calls:")
    print(calls)
    return calls

def readBoard(input):
    print("parsing board...")
    rows=[]
    cols=[]
    index = 0
    for i in range(5):
        for j in range(5):
            index += 1
            cols.append(index)      # TODO: add as a tuple with a bool for the 'flag'
        rows.append(cols)    
        cols=[]
    return rows        


def printBoard(board):
    print("board")
    print(board)
    for r in board:
        print("%d %d %d %d %d" %(r[0],r[1],r[2],r[3],r[4]))
    print("done")



def readData(filename):
    print("reading data...")
    calls = []
    boards = []

    with open(filename, 'r') as infile:
        lines = infile.readlines()
        index = 0
        row = 0
        rows=[]
        for line in lines:
            line = line.strip()
            print("line=%s" % line)
    
            # first row is comma separated list of calls
            if index == 0:
                calls = readCalls(line)
            else:
                if len(line) > 0:
                    rows.append(line)
                    row += 1    
                    if row >= 5:
                        boards.append(readBoard(rows))
                        row=0
                        rows=[]
            index += 1
    
    return (calls, boards)        

    
# find the value "call" on the board and flag as called    
def ProcessCall(call, board):
    return 0


def day4a(filename):

    (calls, boards) = readData(filename)
    
    print("num calls  = %d" % len(calls))
    print("num boards = %d" % len(boards))
    
    for b in boards:
        printBoard(b)
    
    return

    for c in calls:
        for b in boards:
            ProcessCall(c, b)

            win = DetectWinner(b)
            if win > 0:
                print("return = %d" % win * c)


        
day4a("day_04_a_test.txt")
#day4a("day_04_a_input.txt")

#day4b("day_04_b_test.txt")
#day4b("day_04_b_input.txt")

