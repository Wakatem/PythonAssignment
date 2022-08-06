import random

#create database file if non-existent
try:
    file = open("database.txt", "r") 
    file.close()
except FileNotFoundError:
    #create file
    file = open("database.txt", "w")
    file.close()
    
#generate password with range of capital letters and small letters and some symbols
def passwordGenerator():
    password = ""
    for x in range(4):
        password += chr(random.randrange(64, 126))
    return password



def encrypted(password):
    encrypted = ""

    for char in password:
        # if shifted char is between the valid password range
        if ord(char) + 7 <= 126:
            encrypted += chr(ord(char) + 7)
        else:
            #add last char from the valid password range
            encrypted += chr(126)

    return encrypted


def storeCredentials(username, password, dateOfRegistration, latestLogin):
    file = open("database.txt", "a")
    file.write(username+":"+password+":"+dateOfRegistration+":"+latestLogin+"\n")
    file.close()
    
def checkExistingUsername(username):
    file = open("database.txt", "r")
    i = 0
    for line in file:
        #extract username from each user record
        savedUsername = line.split(":")[0]
        if username == savedUsername:
            return i  #username already exists
        i += 1
    return False #username does not exist


def login(value,password):
    file1 = open("database.txt",'r')
    record = file1.readlines()[value]
    username, encryptedPassword, reg_date, latestLogin = record.split(":")
    print (encryptedPassword,encrypted(password))
    if encrypted(password) == encryptedPassword:
        return True
    return False