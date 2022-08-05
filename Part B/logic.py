import random

#create database file
open("database.txt", "w")

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
    file.write(username+":"+password+":"+dateOfRegistration+":"+latestLogin)
    file.close()
    
def checkExistingUsername(username):
    file = open("database.txt", "r")
    for line in file:
        #extract username from each user record
        savedUsername = line.split(":")[0]
        if username == savedUsername:
            return True #username already exists
    return False #username does not exist

