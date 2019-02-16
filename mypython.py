#######################################################
# Name: Travis Laxson
# Date: 16 Feb 2019
# ONID: laxsont
# Email: laxsont@oregonstate.edu
# Description: Python script file that
# performs the follwing actions:
#
# 	1) Create 3 files in directory
#	2) Each file will contain 10 randomly
#	   selected lowercase letters, no spaces
#	3) The eleventh char of each file is
#	   a new line character
#	4) Displays two random integers between
#	   1-42 inclusive and then performs 
#	   multiplication on them before
#	   displaying the product on final line
# 
# Upon execution, the script will begin printing
# the contents of the 3 created files. Next, the 
# values of the two randomly generated numbers 
# separated by newlines will display. Lastly, the 
# script will calculate and display the product of
# the two randomly generated integer values on the
# final line of output.   
#
# Sources:
# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://www.tutorialspoint.com/python/python_functions.htm
# https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
# https://simple.wikipedia.org/wiki/ASCII#/media/File:ASCII-Table-wide.svg
# https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
# https://docs.python.org/3/library/random.html
######################################################
import random as r

# Hard coded file names
FILENAMES = ["The", "Three", "Migos"]

############## FUNCTION ###############
# Name: readFiles
# Description: Opens each of the global
# file names and prints the file contents
# to the terminal.
# Input: NA
# Output: ASCII characters from 3 files
# Returns: NA
#######################################
def readFiles():
	for i in range(3):
		file = open(FILENAMES[i], "r")
		print(file.read(), end="")
		file.close()		


############## FUNCTION ###############
# Name: writeToFile
# Description: Appends or creates file
# if one doesn't already exists each
# ascii character to the file and if
# the last index is reached appends a 
# newline character.
# Input: (3) - file name, ascii, index
# Output: NA
# Returns: NA
#######################################
def writeToFile(fileName, asciiChar, index):
	file = open(fileName, "a+")
	file.write(asciiChar)
	if(index == 9):
		file.write("\n")
	file.close


############## FUNCTION ###############
# Name: getRandomASCIIs 
# Description: Generates 10 randomly
# selected integers beteween 97 - 122.
# and converts them to ascii to pass
# to the write file function.
# Input: NA
# Output: NA
# Returns: Random integer 97 - 122
#######################################
def getRandomASCIIs(fileName):
	for i in range(10):
		value = r.randint(97, 122)	
		writeToFile(fileName, chr(value), i)


############## FUNCTION ###############
# Name: getRandomProduct 
# Description: Generates 2 random int
# values from 1 to 42, inclusive, prints
# them to the console, and then performs
# multiplication before printing the
# product on the third line.
# Input: NA
# Output: NA
# Returns: Random integer 97 - 122
#######################################
def getRandomProduct():
	value1 = r.randint(1, 42)
	value2 = r.randint(1, 42)
	product = value1 * value2
	print(value1)
	print(value2)
	print(product)


############## FUNCTION ###############
# Name: executeScript 
# Description: Contains all of the logic
# to run the script.
# Input: NA
# Output: NA
# Returns: NA
#######################################
def executeScript():
	r.seed()
	for i in range(3):
		getRandomASCIIs(FILENAMES[i])
	readFiles()
	getRandomProduct()


# MAIN FUNCTION #	
def main():
	executeScript()


# RUN PROGRAM #
if __name__ == "__main__":
	main()
