

#functions will be located here


#secures a name from user
def not_blank(question, error_mess):
	valid = False
	# possibly show a button, and the button is only active once you have inputted something

	while not valid:
		response = input(question)

		# if 'name' is not blank, the program will proceed as normal notify user that process has worked.
		if response != "":
			print('name recorded.')
			return response

		# if 'name' is blank, disp[lay error, and repeat
		else:
			print(error_mess)

	#**** Main ****

# Dictionaries / Lists

# Has the User used the program before?

#Loop to get details - how about we make a preset from some options the user chooses from
#then the player will make the character

	#Get Name, and required details (can't be blank)
	name = not_blank('What is your name?', 'Last I checked, names need to be written')

	print(name)
	#Get some information like deltarune!
	
	#Pick hair colour, eye colour, etc for preset
	
	#calculate data and display character
	
	#customise loop
	
	#Finalize character + display final sprite
	
	#ask something meta lmao maybe
	
# 
