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
FILENAMES = ["The", "Three", "Migos"]

############## FUNCTION ###############
# Name: convertNumToASCII
# Description: Takes an integer input
# parameter and converts that value 
# into the ASCII symbol.
# Input: Integer value
# Output: NA
# Returns: ASCII character
#######################################
def writeToFile(fileName, asciiChar):
	file = open(fileName, "a+")
	file.write(asciiChar)
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
	print("NUMBER: " + str(number) + "\nASCII: " + str(asciiChar) + "\n")
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
		print("Random value" + str(i+1) + " = " + str(value))
		asciiChar = convertNumToASCII(value)
		writeToFile(fileName, asciiChar)

############## FUNCTION ###############
# Name: createFile 
# Description: Creates 3 files and 
# writes the result of the ____ to each
# of the three files.
# Input: Name of file to create
# Output: NA
# Returns: NA
#######################################
def createFile(fileName):
	file = open(fileName, "w+")
	file.write("This is the first line of the file\n")
	file.close()

	
def main():
	random.seed()
	
	for i in range(3):
		getRandomASCIIs(FILENAMES[i])
	
#	for i in range(3):
#		createFile("fileName" + str(i))


if __name__ == "__main__":
	main()
