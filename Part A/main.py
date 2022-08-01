import logic


def displaySalariesAVG():
    avgs = logic.salariesAverage()
    print("Admin Average Salary:", str(avgs[0]), " | ", 
          "IT Average Salary:", str(avgs[1]), " | ", 
          "HR Average Salary:", str(avgs[2]), " | ",
          "Sales Average Salary:", str(avgs[3]), " | ",
          "Accounting Average Salary: ", str(avgs[4]), " | ")

def displaySummary():
    Admin, IT, HR, Sales, Accounting = logic.sectionsSummary()
    print("\t\tAdmin\t|\tIT\t|\tHR\t|\tSales\t|\tAccounting")
    print("NO of Males\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(Admin[0], IT[0], HR[0], Sales[0], Accounting[0]))
    print("NO of Females\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(Admin[1], IT[1], HR[1], Sales[1], Accounting[1]))
    print("Total Employees\t  {0}\t\t{1}\t\t{2}\t\t {3}\t\t    {4}".format(Admin[2], IT[2], HR[2], Sales[2], Accounting[2]))


option = 0

while option is not 6:
    print("\n\n=======================================")
    print("Select an option: ")
    print("\t1. Add an employee\n\t2. Remove an employee\n\t3. Change employee's section\n\t4. Salaries average\n\t5. Sections summary\n\t6. Exit")
    print("=======================================")
    option = int(input("input: "))
    
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        displaySalariesAVG()
    elif option == 5:
        displaySummary()
    elif option == 6:
        break
    else:
        print("Choose one of the provided options")