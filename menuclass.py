from rgfunc import *

class MainMenu(object):
	optList = ["List","View Details","Search","New","Edit","Delete"]
	sldopt = 0
	sldm =""
	
	
	def __init__(self):#,userName):
		#self.userName= userName
		pass
	def menu(self):
		stline()
		print "MAIN MENU"
		stline()
		br()
		for i in range(1,len(self.optList)+1):
			print str(i)+": " +self.optList[i-1]
		br()
		self.optinput()

	#def act(self,sopt):
		#print self.optList[sopt-1]

	def checkInput(self,inp):
		if inp.lower() == "b" or inp.lower() == "back":
			stline()
			print "BACK MENU"
			stline()
			br()
			return True
		try:
			inp = int(inp)
			if inp<=0 or inp >=len(self.optList)+1:
				print "Input Out of Range"
				br()
				return False
			self.printTitle(inp)
			return True
		except ValueError:
			print "Invalid Input"
			br()
			return False

	def optinput(self):
		opt = raw_input("Enter your option: ")
		br()
		if not self.checkInput(opt):
			self.menu()
		else:
			try:
				self.sldopt=int(opt)
			except:
				self.sldm = opt
	def printTitle(self,inp):
		stline()
		print self.optList[inp-1],"Employees"
		stline()
		
if __name__ == "__main__":
	print "Error-Invalid File to Run- Please Run main.py."
	exit()
