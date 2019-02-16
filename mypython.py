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
def createFile(fileName):
	file = open(fileName + ".txt", "w+")
	file.write("This is the first line of the file\n")
	file.close()
	
def main():
	fileName1 = "logfile1"
	fileName2 = "logfile2"
	fileName3 = "logfile3"
	
	for i in range(3):
		createFile("fileName" + str(i))

if __name__ == "__main__":
	main()
