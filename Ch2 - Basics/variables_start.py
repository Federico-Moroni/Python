# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#

# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
from traceback import print_tb


myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False, 5, 4, 3, 2, 1]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# re-declaring a variable works
# myint="abc"
# print(myint)
# to access a member of a sequence type, use []
# print(mylist[2])
# print(mytuple[1])
# print(mylist[1:5])
# use slices to get parts of a sequence
# print(mylist[1:10:3])
# you can use slices to reverse a sequence
# print(mylist[::-1])
# dictionaries are accessed via keys
# print(mydict["one"])
# ERROR: variables of different types cannot be combined
# Claramente no puedo sumar strings con int, pero puedo usar la function str() para transformar un numero a string.
print("string type" + str(123))

# Global vs. local variables in functions
def someFunction():
    global mystr
    mystr= "def"
    print(mystr)

someFunction()
print(mystr)

# delete mystr from everywhere
del mystr
print(mystr)