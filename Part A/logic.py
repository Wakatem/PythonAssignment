class Employee:
    def __init__(self, name, id, salary, section, hoursPerWork, male):
        self.name = name
        self.id = id
        self.salary = salary
        self.section = section
        self.hoursPerWork = hoursPerWork
        self.male = male

Employees = [
    Employee("James", 782136, 70000, "Admin", 100, True),
    Employee("Mark", 554723, 55000, "Admin", 90, True),
    Employee("Ali", 116573, 10000, "IT", 40, True),
    Employee("Mohammed", 873654, 20000, "IT", 60, True),
    Employee("Fatima", 445236, 30000, "HR", 84, False),
    Employee("Khalid", 229475, 15000, "Sales", 56, True),
    Employee("Ayesha", 792643, 60000, "IT", 93, False),
    Employee("Maria", 888130, 20000, "Accounting", 55, False),
    Employee("Saad", 913746, 35000, "HR", 67, True),
    Employee("Riya", 546293, 45000, "Accounting", 50, False),
    Employee("Rahul", 232903, 50000, "Sales", 61, True),
    Employee("Jazlyn", 446839, 65000, "Sales", 75, False)
]


sections = ['Admin','IT','Sales','HR','Accounting']


def addEmployee(id):    
     
    name = input("Enter Name of new Employee:\n")
    salary = int(input("Enter Salary of new Employee:\n"))
    section = input("Enter Section of new Employee:\n")
    hoursPerWork = int(input("Enter Hours per Work of new Employee:\n"))
    male = ""
    
    while True:
        gender = input("Enter Gender of new Employee ['F' for female, 'M' for male]:")
        if gender == "M".casefold():
            male = True
            break 
        elif gender == "F".casefold(): 
            male = False
            break
        else:
            print("Kindly enter F or M")
        

    Employees.append(Employee(name,id,salary,section,hoursPerWork, male))
    
    print("Employee added successfully.\n")




def removeEmployee(empPos):
    Employees.pop(empPos)
    print("Employee Removed successfully.") 


def viewEmployeeList():
    print("\nEmployees List:\n")
    for obj in Employees:
        print(obj.name,obj.id,obj.salary,obj.section,obj.hoursPerWork,obj.male)


def changeSalary(empPos, new_salary):
    Employees[empPos].salary = new_salary
    print("\nEmployee Salary has been updated Successfully.\n")    


def changeSection(empPos,new_section):
    Employees[empPos].section = new_section
    print("\nEmployee Section has been updated Successfully.\n")    



def salariesAverage():
    Admin_average = 0; Admin_count = 0
    IT_average = 0; IT_count = 0
    HR_average = 0; HR_count = 0
    Sales_average = 0; Sales_count = 0
    Accounting_average = 0; Accounting_count = 0

    for employee in Employees:
        if employee.section == "Admin":
            Admin_average += employee.salary
            Admin_count += 1

        elif employee.section == "IT":
            IT_average += employee.salary
            IT_count += 1

        elif employee.section == "HR":
            HR_average += employee.salary
            HR_count += 1

        elif employee.section == "Sales":
            Sales_average += employee.salary
            Sales_count += 1

        else:
            #Accounting
            Accounting_average = employee.salary
            Accounting_count += 1
    
    Admin_average = Admin_average / Admin_count
    IT_average = IT_average / IT_count
    HR_average = HR_average / HR_count
    Sales_average = Sales_average / Sales_count
    Accounting_average = Accounting_average / Accounting_count

    return [Admin_average, IT_average, HR_average, Sales_average, Accounting_average]


def sectionsSummary():
    Admin_male = 0; Admin_female = 0
    IT_male = 0; IT_female = 0
    HR_male = 0; HR_female = 0
    Sales_male = 0; Sales_female = 0
    Accounting_male = 0; Accounting_female = 0

    for employee in Employees:
        if employee.section == "Admin":
            if employee.male is True:
                Admin_male += 1
            else:
                Admin_female += 1

        elif employee.section == "IT":
            if employee.male is True:
                IT_male += 1
            else:
                IT_female += 1

        elif employee.section == "HR":
            if employee.male is True:
                HR_male += 1
            else:
                HR_female += 1

        elif employee.section == "Sales":
            if employee.male is True:
                Sales_male += 1
            else:
                Sales_female += 1

        else:
            #Accounting
            if employee.male is True:
                Accounting_male += 1
            else:
                Accounting_female += 1
    
    #tuples for each section: numbers of males, numbers of females, number of employees per section
    Admin = (Admin_male, Admin_female, Admin_male+Admin_female)
    IT = (IT_male, IT_female, IT_male+IT_female)
    HR = (HR_male, HR_female, HR_male+HR_female)
    Sales = (Sales_male, Sales_female, Sales_male+Sales_female)
    Accounting = (Accounting_male, Accounting_female, Accounting_male+Accounting_female)

    return [Admin, IT, HR, Sales, Accounting]

def getID(message):
    matchingID = False
    empPos = 0

    while matchingID is False:
            try:
                id = int(input(message))

                pos = 0
                for emp in Employees:
                    if id == emp.id:
                        matchingID = True
                        empPos = pos
                        break
                    pos += 1

                if matchingID is False:
                    print("ID not found.")

            except ValueError:
                print("Enter an ID containing integers only.")


    return empPos

