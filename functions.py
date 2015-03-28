from rgfunc import *

def printEmp(employees):
	n = 1
	for name in employees:
		print n, ": ", name.fullname()
		n +=1
	br()



def new_emp(Employee,employees):
	br()
	print "Enter New Employees Details"
	employee = Employee(raw_input("Enter new employee's frist name: "))
	employee.lastname = raw_input("Enter new employee's last name: ")
	employee.city = raw_input("Enter name of city: ")
	employee.country = raw_input("Enter name of country: ")
	employee.day =  get_int("Enter the date of birth: ")
	employee.month = get_int("Enter the month of birth: ")
	employee.year =  get_int("Enter the year of birth: ")
	employees.append(employee)
	br()

def det_emp(employee):
	br()
	stline()
	print employee.fullname()
	stline()
	br()
	print "First Name: ",employee.name
	print "Last Name: ",employee.lastname
	print "City: ",employee.city
	print "Country: ",employee.country
	print "Date of Birth:",employee.dateofbirth()
	br()
	
def vd_emp(employees):
	if len(employees) == 0:
		br()
		print "Empty - nothing to View"
		br()
	else:
		br()
		printEmp(employees)
		vd_empl = get_int("choose employee to vew details: ")
		br()
		det_emp(employees[vd_empl-1])
		

def list_emp(employees):
	if len(employees) == 0:
		br()
		print "Empty - nothing to View"
		br()
	else:
		br()
		printEmp(employees)
	
def del_emp(employees):
	if len(employees) == 0:
		br()
		print "Empty - nothing to Delete"
		br()
	else:
		printEmp(employees)
		stline()
		del_name = raw_input("Which employee you want to delete: ")
		try:
			del_name = int(del_name)
			del employees[del_name-1]
			printEmp(employees)
			stline()
			br()
		except:
			br()
			print "Invalid Input"
			br()
		
def srch_emp(employees):
	listName = []
	num = []
	br()
	sr_name = raw_input("Enter name of employee you want to search: ")
	br()
	no = 1
	for name in employees:
		if sr_name.lower() == name.name.lower():
			listName.append(name.fullname())
			num.append(no)
		no +=1
		
	if len(listName) == 0:
		br()
		print "Nothing Found, Try Again"
		br()
	else:
		n= 1
		for name in listName:
			print num[n-1] , ": " ,name
			n +=1
	br()

def edit_emp(employees):
	pass

if __name__ == "__main__":
	print "Error-Invalid File to Run- Please Run main.py."
	exit()
