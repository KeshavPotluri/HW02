#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def printChar(s):
	print(s),

def printLastChar(y):
	print(y)

def printLine(firstChar, secChar):
	printChar(firstChar)
	printChar(secChar)
	printChar(secChar)
	printChar(secChar)
	printChar(secChar)

def printHorizontalTwice(firstChar, secChar):
	printLine(firstChar,secondChar)
	printLine(firstChar,secondChar)

def printHorizontalFourTimes(firstChar, secChar):
	printHorizontalTwice(firstChar, secChar)
	printHorizontalTwice(firstChar, secChar)

def printHorizontal(isTwice, firstChar, secChar):
	if isTwice:
		printHorizontalTwice(firstChar, secChar)
	else:
		printHorizontalFourTimes(firstChar, secChar)
	printLastChar(firstChar)

def printVertical(isTwice):
	printHorizontal(isTwice, "|", " ")
	printHorizontal(isTwice, "|", " ")
	printHorizontal(isTwice, "|", " ")
	printHorizontal(isTwice, "|", " ")
	printHorizontal(isTwice, "+", "-")


def printVerticalTwice(isTwice):
	printVertical(isTwice)
	printVertical(isTwice)

def two_by_two():
	printHorizontal(True,"+", "-")
	printVerticalTwice(True)

def four_by_four():
	printHorizontal(False,"+", "-")
	printVerticalTwice(False)
	printVerticalTwice(False)

# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")


    



if __name__ == "__main__":
    main()