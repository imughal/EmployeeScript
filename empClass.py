from rgfunc import *

class Employee(object):
	year = 0
	month = 0
	day = 0
	city = ""
	country = ""
	lastname = ""
	

	
	def __init__(self,name):
		self.name = name
		
	
	def dateofbirth(self):
		return str(self.day)+"/"+str(self.month)+"/"+str(self.year)
	#fullname = name," ",lastname
	def fullname(self):
		return str(self.name)+" "+str(self.lastname)


if __name__ == "__main__":
	print "Error-Invalid File to Run- Please Run main.py."
	exit()
