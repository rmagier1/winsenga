"""
    Problem 2: Given 3 int values, a b c, return their sum. 
    However, if one of the values is 13 then it does not
    count towards the sum and values to its right do not count. 
    So for example, if b is 13, then both b and c do
    not count. create a function called panda to execute the tasks below as illustrated:
    panda (1, 2, 3) -> 6
    panda (1, 2, 13) -> 3
    panda (1, 13, 3) ->1
"""

from random import *

def main():
    """main used for testing"""
    for i in range(10):
        a = randrange(1,20) #get 3 random integers for testing
        b = randrange(1,20)
        c = randrange(1,20)
        panda_val = panda(a,b,c)
        print "panda(%d,%d,%d) -> %d" %(a,b,c,panda_val)

def panda(a,b,c):
    total = 0
    ls = [a,b,c]
    for item in ls:
        if item == 13:
            break
        else:
            total += item

    return total


main()
