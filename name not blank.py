#functions


#possibly show a button, and the button is only active once you have inputten something
def not_blank(question, error_mess):
	valid = False

	while not valid:
		response = input(question)
		
		if response != "":
			print('name recorded.')
			return response
		else:
			print(error_mess)

#main

name = not_blank("What is your name?", "Last I checked, names need to be written")