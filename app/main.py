from cleaner import *

if(__name__=='__main__'):
	filename = str(input("Enter the name of file :\n"))
	count = code_cleaner(filename)
	code_execute(filename)
