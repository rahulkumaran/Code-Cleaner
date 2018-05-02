from cleaner import *

if(__name__=='__main__'):
	filename = str(input("Enter the name of file :\n"))
	exec_filename = str(input("Enter the name of your executable:\n"))
	count = code_cleaner(filename)
	code_execute(exec_filename)
