import logic

def addEmployee():
    
    #while given id is not available 
    idExists = True
    while idExists is True :
        try:
            id = int(input("\nKindly enter id of new employee containing 6 digits:\n"))

            #Check to accept only ID of 6 digits
            if len(str(id)) != 6:
                print("ID not accepted.")


            #Check if id already exists
            pos = 0
            for emp in logic.Employees:
                if id == emp.id:          
                    print("ID already Exists.")
                    idExists = True
                    break
                pos += 1
            
            #Given id is new
            idExists = False
            logic.addEmployee(id)

        except ValueError:
            print("Enter an ID containing integers only.")   



def removeEmployee():
    empPos = logic.getID("\nEnter ID of Employee to Remove:\n")
    logic.removeEmployee(empPos)



def checkSalary():
    empPos = logic.getID("Enter ID of Employee to change his/her Salary:")

    new_salary = 0
    while True:
        try:
            new_salary = int(input("Enter new Salary:"))
            break
        except ValueError:
            print("Enter a salary of digits only")
    

    #if both inputs are valid
    logic.changeSalary(empPos, new_salary)


def checkSection():
    empPos = logic.getID("Enter ID of Employee to change his/her Section:")

    new_section = ""
    matchingSection = False

    while matchingSection is False:
        new_section = input("Enter new Section:")

        for section in logic.sections:
            if new_section == section:
                matchingSection = True
        
        if matchingSection is False:
            print("Section does not exist.")

    #if both inputs are valid
    logic.changeSection(empPos, new_section)



def displaySalariesAVG():
    avgs = logic.salariesAverage()
    print("Admin Average Salary:", str(avgs[0]), " | ", 
          "IT Average Salary:", str(avgs[1]), " | ", 
          "HR Average Salary:", str(avgs[2]), " | ",
          "Sales Average Salary:", str(avgs[3]), " | ",
          "Accounting Average Salary: ", str(avgs[4]), " | ")


def displaySummary():
    #get number of employees, number of male and females per section
    Admin, IT, HR, Sales, Accounting = logic.sectionsSummary()
    
    #list of average salary in all sections (as integers)
    averages = [ int(average) for average in logic.salariesAverage()]
    
    #calculate total average salary of all sections
    sectionsAverage = 0
    for average in averages:
        sectionsAverage += average
    sectionsAverage = int(sectionsAverage / len(averages))

    print("\t\tAdmin\t|\tIT\t|\tHR\t|\tSales\t|\tAccounting")
    print("NO of Males\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(Admin[0], IT[0], HR[0], Sales[0], Accounting[0]))
    print("NO of Females\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(Admin[1], IT[1], HR[1], Sales[1], Accounting[1]))
    print("Salary Average\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(averages[0], averages[1], averages[2], averages[3], averages[4]))
    print("Total Employees\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(Admin[2], IT[2], HR[2], Sales[2], Accounting[2]))
    print("Total company employees:", str(Admin[2]+IT[2]+HR[2]+Sales[2]+Accounting[2]))
    print("Total average of sections salaries:", str(sectionsAverage))



option = 0

#User Menu
while option is not 8:
    print("\n\n=======================================")
    print("Select an option: ")
    print("\t1. Add an employee\n\t2. Remove an employee\n\t3. View list of employees\n\t4. Change employee's salary\n\t5. Change employee's section\n\t6. Salaries average\n\t7. Sections summary\n\t8. Exit")
    print("=======================================")
    option = int(input("input: "))
    
    if option == 1:
        addEmployee()
    elif option == 2:
        removeEmployee()
    elif option == 3:
        logic.viewEmployeeList()
    elif option == 4:
        checkSalary()
    elif option == 5:
        checkSection()
    elif option == 6:
        displaySalariesAVG()
    elif option == 7:
        displaySummary()
    else:
        print("Choose one of the provided options")