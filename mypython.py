#######################################################
# Name: Travis Laxson
# Date: 15 Feb 2019
# ONID: laxsont
# Email: laxsont@oregonstate.edu
# Description: Python script file that
# performs the follwing actions:
# 	1) Create 3 files in directory
#	2) Each file contains 10 random chars from
#	   the lowercase alphabet, no spaces
#	3) Final, eleventh char of each file is
#	   a new line character
#	4) Generate random integer values and 
#  	   perform basic arithmetic on them
# 
# Upon execution the script will first print 
# out the contents of the 3 created files. Then
# the values of the two randomly generated numbers 
# separated by newlines will display. Lastly, the 
# script will calculate and display the product of
# the two randomly generated integer values on the
# final line of output.   
#
######################################################
import random
import sys

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
		sys.stdout.flush()
		print(open(FILENAMES[i]).read(), end="")
		

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
# Name: convertNumToASCII
# Description: Takes an integer input
# parameter and converts that value 
# into the ASCII symbol.
# Input: Integer value
# Output: NA
# Returns: ASCII character
#######################################
def convertNumToASCII(number):
	asciiChar = chr(number)
	return asciiChar

############## FUNCTION ###############
# Name: getRandomASCIIs 
# Description: Generates 10 randomly
# selected integers beteween 97 - 122.
# Input: NA
# Output: NA
# Returns: Random integer 97 - 122
#######################################
def getRandomASCIIs(fileName):
	for i in range(10):
		value = random.randint(97, 122)	
		asciiChar = convertNumToASCII(value)
		writeToFile(fileName, asciiChar, i)

	
def main():
	random.seed()
	
	for i in range(3):
		getRandomASCIIs(FILENAMES[i])
			
	readFiles()

	
if __name__ == "__main__":
	main()
