import logic
import time
import datetime
import os


def delay(seconds, message=""):
    start = time.time()
    duration = 0
    halfway = False
    while int(duration) != seconds:
        duration = int(time.time() - start)
        if halfway is False:
            if duration == 30:
                halfway = True
                print(message)



def register():
    while True:
        username = input("Enter your username: ")

        #check username length
        if len(username) < 4:
            print("Enter a username of minimum 4 characters")
        
        elif logic.checkExistingUsername(username) is False:
        
            #if username is available, store credentials
            randomPassword = logic.passwordGenerator()
            encryptedPassword = logic.encrypted(randomPassword)
            dateOfRegistration = str(datetime.datetime.now())
            latestLogin = dateOfRegistration
            logic.storeCredentials(username, encryptedPassword, dateOfRegistration, latestLogin)
        
            #display password
            print("Your password is:", randomPassword, " |  (This password is shown for one minute)")
            delay(60, "30 seconds passed")
        
            print("One minute passed. Going back to menu.")
            delay(3)
            os.system("cls" if os.name == "nt" else "clear") #clear screen
            break



#User Menu
option = 0
while True:
    print("\n\n=======================================")
    print("Select an option: ")
    print("\t1. Register\n\t2. Login\n\t3. Exit")
    print("=======================================")
    try:

        option = int(input("input: "))

        if option == 1:
            register()
        elif option == 2:
            #login()
            pass
        elif option == 3:
            break
        else:
            print("Choose one of the provided options")
    except ValueError:
        print("Enter the number of the option you want")