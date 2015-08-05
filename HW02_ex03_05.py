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

def printCharacter(i, firstChar, secChar):
	if i >0:
		if(i==1 or i%5 == 1):
			if(i==1):
				printLastChar(firstChar)
			else:
				printChar(firstChar)
				printCharacter(i-1, firstChar, secChar)
		else:
			printChar(secChar)
			printCharacter(i-1, firstChar, secChar)

	
def printLine(numberOfBoxes, firstChar, secChar):
	i = numberOfBoxes*5 + 1
	printCharacter(i, firstChar, secChar)



def printVerticalLine(j,numberOfBoxes):
  	if j>0:
		if(j==1 or j%5 == 1) :
			printLine(numberOfBoxes, "+", "-")
			printVerticalLine(j-1, numberOfBoxes)
		else:
			printLine(numberOfBoxes, "|", " ")
			printVerticalLine(j-1, numberOfBoxes)

def printVerticalLines(numberOfBoxes):
	j = numberOfBoxes*5 + 1
	printVerticalLine(j,numberOfBoxes)

def two_by_two():
	printVerticalLines(2)

def two_by_two():
	printVerticalLines(4)


# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")

	two_by_two()
	four_by_four() 



if __name__ == "__main__":
    main()