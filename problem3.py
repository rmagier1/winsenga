"""
    Problem 3: Create a file called "age.txt" with 10 records each having a name and age. i.e.:
tom, 24
carol, 30
Ronald 15 e.t.c.

You are to write a program that will read the file and return the names of people above 20 years.
"""


def main():
    names = readFile("age.txt")
    above_20 = findNames(names)
    print "Names above 20 from file age.txt: \n", ", ".join(above_20)

def findNames(names):
    over_20 = []
    for item in names:
        if item[1] > 20:
            over_20.append(item[0])

    return over_20

def readFile(filename):
    names = []
    file = open(filename,"r")
    for line in file:
        line = line.strip().split(",")
        line[1] = int(line[1])
        names.append(line)

    return names

main()