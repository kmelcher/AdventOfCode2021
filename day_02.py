#!/usr/bin/python

# Advent of Code 2021

# day 02 A

import math


def day2a(filename):

    horiz = 0
    depth = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            print("line=%s" % line)

            tokens = line.split()
            if len(tokens) == 2:
                if (tokens[0] == "forward"):
                    horiz += int(tokens[1])
                if (tokens[0] == "down"):
                    depth += int(tokens[1])
                if (tokens[0] == "up"):
                    depth -= int(tokens[1])

    print("horiz = %d" % horiz)
    print("depth = %d" % depth)
    print("result = %d" % (horiz*depth))

def day2b(filename):

    horiz = 0
    depth = 0
    aim = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            print("line=%s" % line)

            tokens = line.split()
            if len(tokens) == 2:
                if (tokens[0] == "forward"):
                    horiz += int(tokens[1])
                    depth += (aim * int(tokens[1]))
                if (tokens[0] == "down"):
                    aim += int(tokens[1])
                if (tokens[0] == "up"):
                    aim -= int(tokens[1])

    print("horiz = %d" % horiz)
    print("depth = %d" % depth)
    print("result = %d" % (horiz*depth))


#day2a("day_02_a_test.txt")
#day2a("day_02_a_input.txt")

day2b("day_02_a_test.txt")
day2b("day_02_a_input.txt")

