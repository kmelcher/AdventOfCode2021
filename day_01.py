#!/usr/bin/python

# Advent of Code 2021

# day 01 A
# count the number of times a depth measurement increases from the 
# previous measurement. (There is no measurement before the first 
# measurement.)

import math


def day1a(filename):
    prev = 0
    increaseCount = 0
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            print("line=%d" % int(line))
            if prev != 0:
                if int(line) > prev:
                    increaseCount += 1
                    print("increased")
                else:
                    print("same or lower")
            prev = int(line)

    print("increase count is %d" % increaseCount)



# use a 3 value sliding window and average the 3 values
# then calc the sum and detect number of increases
def day1b(filename):
    prev = 0
    nextSlot = 0
    maxSlots = 3
    slots = [-1,-1,-1] 
    
    increaseCount = 0
    
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            print("line=%d" % int(line))
    
            slots[nextSlot] = int(line)
            nextSlot = (nextSlot+1) % maxSlots

            # only start calcing once we fill all the slots            
            if (slots[0] != -1 and slots[1] != -1 and slots[2] != -1):
            
                # calc sliding window
                sum = slots[0] + slots[1] + slots[2]
                print("Sum is %d" % sum)           
            
                if prev != 0:
                    if sum > prev:
                        increaseCount += 1
                        print("increased")
                    else:
                        print("same or lower")

                prev = sum

    print("increase count is %d" % increaseCount)


#day1a("day_01_a_test.txt")
# correct 7
#day1a("day_01_a_input.txt")

day1b("day_01_a_test.txt")
day1b("day_01_a_input.txt")