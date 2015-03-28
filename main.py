#!/usr/bin/python

from menuclass import *
from empClass import *
from functions import *


employees = []

mainMenu = MainMenu()



while True:
	cmd = raw_input("What you want to DO: ")
	br()
	if cmd.lower() == "q":
		print "Quiting Now......"
		waits()
		exit()
	elif cmd.lower() == "m":

		while True:
			sldOpt = ""
			mainMenu.sldopt = 0
			mainMenu.menu()
			sldOpt = mainMenu.optList[mainMenu.sldopt - 1]
			if mainMenu.sldopt == 0:
				break
			if sldOpt == "New":
				new_emp(Employee,employees)
			elif sldOpt == "List":
				list_emp(employees)
			elif sldOpt == "Search":
				srch_emp(employees)
			elif sldOpt == "Delete":
				del_emp(employees)
			elif sldOpt == "Edit":
				edit_emp(employees)
			elif sldOpt == "View Details":
				vd_emp(employees)

	elif cmd.lower() == "help" or cmd.lower() =='h':
		help()
		
	else:
		print 'Error... Please enter "Help" or "H" to get help'

