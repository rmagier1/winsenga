"""
problem 1 - 
Given a string, return a version without the first and last characters, so "Hello" yields "ell".
a) Create a function to execute the above for 'Compuscan'
b) Reverse the order of the string generated above.
"""

def main():
    word = "Compuscan"
    modified = modifyWord(word)
    reverse = reverseWord(word)
    print "Word: %s" %(word)
    print "Word without first and last characters: %s" %(modified)
    print "Word reversed: %s" %(reverse)

def modifyWord(word):
    return word[1:len(word)-1]

def reverseWord(word):
    if len(word) <= 1:
        return word

    return reverseWord(word[1:]) + word[0]

main()