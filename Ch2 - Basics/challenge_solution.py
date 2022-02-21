# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

from ast import Break
from operator import truediv


def is_palindrome(teststr):
    if teststr == teststr[::-1]:
        return True
    return False


run = True
while(run):
    teststr = input("Please enter your word, sentence or numbers or exit")

    if teststr == "exit":
        run = False
        break

    teststr = teststr.lower()

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print("Palindrome result:", is_palindrome(newstr))
