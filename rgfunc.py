#!/usr/bin/python
def br():
	print ""
	
def stline():
	print "------------------------"
	

def help():
	stline()
	print "Help"
	stline()
	br()
	print "'m' or 'M' 	'Main Menu'"
	print "'q'		'Quit programm'"

def waits():
	try:
		n = 1
		while n<(9999 * 999):
			n = n +1
	except:
		print "print Error"

def get_int(message):
	while True:
		try:
			new_int=int(raw_input(message))
			break
		except:
			print "Invalid Input"
	return new_int


if __name__ == "__main__":
	print "Error-Invalid File to Run- Please Run main.py."
	print get_int("Enter: ")
	exit()
