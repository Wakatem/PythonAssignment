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
