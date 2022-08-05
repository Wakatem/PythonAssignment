import logic
import time

option = 0

while option is not 3:
    print("\n\n=======================================")
    print("Select an option: ")
    print("\t1. Register\n\t2. Login\n\t3. Exit")
    print("=======================================")
    option = int(input("input: "))
    
    if option == 1:
        while True:
            username = input("Enter your username: ")

            if len(username) < 4:
                print("Enter a username of minimum 4 characters")

            elif logic.checkExistingUsername(username) is False:
                
                #if username is available, store credentials
                randomPassword = logic.passwordGenerator()
                encryptedPassword = logic.encrypted(randomPassword)
                dateOfRegistration = ""
                latestLogin = dateOfRegistration
                logic.storeCredentials(username, encryptedPassword, dateOfRegistration, latestLogin)
                
                print("Your password is:", randomPassword, " |  (This password is shown for one minute)")
                #while still not a minute passed
                start = time.time()
                while time.time() - start != 60:
                    pass
                break


    elif option == 2:
        pass
    elif option == 3:
        break
    else:
        print("Choose one of the provided options")