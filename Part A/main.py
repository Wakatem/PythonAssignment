import logic


def checkSection():

    matchingID = False
    matchingSection = False

    while matchingID is False:
        try:
            id = int(input("Enter ID of Employee to change his/her Section:"))

            for emp in logic.Employees:
                if id == emp.id:
                    matchingID = True
            
            if matchingID is False:
                print("ID not found.")

        except ValueError:
            print("Enter an ID containing integers only.")

    while matchingSection is False:
        new_section = input("Enter new Section:")

        for section in logic.sections:
            if new_section == section:
                logic.changeSection(id,new_section)
                matchingSection = True
        
        if matchingSection is False:
            print("Section does not exist.")





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
while option is not 6:
    print("\n\n=======================================")
    print("Select an option: ")
    print("\t1. Add an employee\n\t2. Remove an employee\n\t3. Change employee's salary\n\t4. Change employee's section\n\t5. Salaries average\n\t6. Sections summary\n\t7. Exit")
    print("=======================================")
    option = int(input("input: "))
    
    if option == 1:
        logic.addEmployee()
    elif option == 2:
        logic.removeEmployee()
    elif option == 3:
        logic.changeSalary()
    elif option == 4:
        checkSection()
    elif option == 5:
        displaySalariesAVG()
    elif option == 6:
        displaySummary()
    elif option == 7:
        break
    else:
        print("Choose one of the provided options")