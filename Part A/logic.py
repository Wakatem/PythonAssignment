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

