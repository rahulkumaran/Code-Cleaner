from cleaner import *

if(__name__=='__main__'):

	choice = str(input("Type 1 => Code cleaning\nType 2 => For code execution\nType 3 => For syntax lookup\nEnter Choice: "))

	if(choice == "1"):
		filename = str(input("Enter the name of file :\n"))
		count = code_cleaner(filename)

	elif(choice == "2"):
		filename = str(input("Enter the name of file :\n"))
		code_execute(filename)

	elif(choice == "3"):
		user_choice = str(input("Type 1 => To get a particular concept in a programming langauge\nType 2 => To get all concepts of a particular language\nEnter choice: "))

		if(user_choice == "1"):
			user_search = str(input("What topic do you want to search about? For example, if you want to understand how to use the print function in python simply type \"print in python\"\n"))
			user_language = ""
			data = syntax_lookup(0, user_search, user_language)
		else:
			user_search = ""
			user_language = str(input("Enter the language about which you want to learn all concepts:\n"))
			data = syntax_lookup(1, user_search, user_language)
		for i in range(0,len(data)):
			print(data[i])

	else:
		print("Enter a valid option\n")
