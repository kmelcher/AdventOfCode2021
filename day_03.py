#!/usr/bin/python

# Advent of Code 2021

# day 03 

import math

# calc gama and epsilon rate 

def day3a(filename):

    numSamples = 0
    counts = []

    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            print("\nline=%s" % line.strip())
            numSamples += 1
            # line contains string of "bits"
            # "0100110"
            # File has consistent line lenth, but can be 5 or 12 (allow arbitrary)

            # on first line, initialize size of counter list
            if numSamples == 1:
                for char in line.strip():
                    counts.append(0)

            index = 0
            for char in line.strip():
                print("char is %c" % char)
                if (char == '1'):
                    counts[index] += 1
                index += 1    

            for count in counts:
                print("  %d" % count)

        print("Final Results samples=%d" % numSamples)
        gamma = ""
        epsilon = ""
        for count in counts:
            print("  %d" % count)
            if count > (numSamples/2):
                gamma += "1"
                epsilon += "0"        
            else:
                gamma += "0"
                epsilon += "1"        
        print("gamma = %s %d" % (gamma, int(gamma,2)))
        print("epsilon = %s %d " % (epsilon, int(epsilon,2)))
        print("Result is %d" %  (int(gamma,2)*int(epsilon,2)))


    #print("horiz = %d" % horiz)
    #print("depth = %d" % depth)
    #print("result = %d" % (horiz*depth))


#-----------------------------------------------------------------
# part Two
#-----------------------------------------------------------------

# load all the values into a list and return the list
def loadValues(filename):
    values = []
    with open(filename, 'r') as infile:
        values = infile.readlines()
        print("loaded %d values" % len(values))
    return values

# return 0/1 based on which bit is most common in specified bit position (0 based index)
def MostCommonBit(values, bitPosition):
    zeroCount = 0;
    oneCount = 0;
    for v in values:
        v = v.strip()
        print("v   is %s" % v)
        print("bit is %s" % (v[bitPosition]))
        if v[bitPosition] == '0':
            zeroCount += 1
        else: 
            oneCount += 1

    if (oneCount>=zeroCount):
        return '1'
    else:
        return '0'


# return 0/1 based on which bit is most common in specified bit position (0 based index)
def LeastCommonBit(values, bitPosition):
    zeroCount = 0;
    oneCount = 0;
    for v in values:
        v = v.strip()
        print("v   is %s" % v)
        print("bit is %s" % (v[bitPosition]))
        if v[bitPosition] == '0':
            zeroCount += 1
        else: 
            oneCount += 1

    if (oneCount<zeroCount):
        return '1'
    else:
        return '0'


def FilterBits(values, bitPosition, bitValue):
    print("filter count in %d, pos %d, value %s" % (len(values), bitPosition, bitValue))
    newValues = []
    
    for v in values:
        if v[bitPosition] == bitValue:
            newValues.append(v)
    print("filter count out %d, pos %d, value %s" % (len(newValues), bitPosition, bitValue))            
    return newValues

def ShowValues(values):
    print("Values left (%d of them)" % len(values))
    for v in values:
        print("v   is %s" % v.strip())
    print("")


def calc_o2_gen(filename):
    numSamples = 0
    values = []

    values = loadValues(filename)
    
    ShowValues(values)
    maxBits = len(values[0].strip())
    print("check...loaded %d values" % len(values))
    print("maxBits is %d" % maxBits)


    for i in range(0,maxBits):
        mcb = MostCommonBit(values, i)    
        print("pos %d most common bit is %s" % (i,mcb))
        values = FilterBits(values, i, mcb)
        print("post filter list")
        ShowValues(values)
        if len(values) == 1:
            print("Done")
            print("result %s %d" % (values[0], int(values[0],2)))
            return int(values[0],2)

def calc_co2_scrub(filename):
    print("co2 Scrubber......")
    numSamples = 0
    values = []
    values = loadValues(filename)
    
    ShowValues(values)
    maxBits = len(values[0].strip())
    print("check...loaded %d values" % len(values))
    print("maxBits is %d" % maxBits)


    for i in range(0,maxBits):
        lcb = LeastCommonBit(values, i)    
        print("pos %d least common bit is %s" % (i,lcb))
        values = FilterBits(values, i, lcb)
        print("post filter list")
        ShowValues(values)
        if len(values) == 1:
            print("Done")
            print("result %s %d" % (values[0], int(values[0],2)))
            return int(values[0],2)

def day3b(filename):
    o2 = calc_o2_gen(filename)
    co2 = calc_co2_scrub(filename)

    print( "o2=%d, c02=%d, result = %d" % (o2, co2, o2*co2))


        
#day3a("day_03_a_test.txt")
#day3a("day_03_a_input.txt")

day3b("day_03_a_test.txt")
day3b("day_03_a_input.txt")

