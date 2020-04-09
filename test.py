import re
import os
import random
import string


users = {}
userD = list()
randomLetters = string.ascii_letters

#function to create Dictionary to store data
def userDet(fname, lname, email):
    first_name = fname.strip()
    last_name = lname.strip()
    email = email.strip()

    full_det = {'first name': first_name, 'last name': last_name, 'email': email}
    return full_det

#function accepts input from the user and stores them in strings.
def userDetails():
    fname = input("Enter First name: ")
    userD.append(fname)
    lname = input("Enter Last name: ")
    userD.append(lname)
    email = input("Enter email: ")
    userDet(fname, lname, email)
    userD.append(email)
    #validation
    if email not in users.keys():
        users[email] = userDet(fname, lname, email)
    else:
        print('Sorry the email exist already. If you are a new user please check email and re-enter details again')
        userDetails()
    createPassword()

#creates password
def createPassword():
    password = ''
    first = userD[0]
    last = userD[1]
    password += (first[:2])
    password += (last[-2:])
    password += "".join(random.choice(randomLetters) for i in range(5))
    print('User password is: {}'.format(password))
    feedback = input("Do you like the generated password (Y / N): ")
    displayUserDetails(feedback)

#password verification
def verifyPassword():
    verification = 'false'
    password = input('Please enter password: ')
    if len(password) >= 7:
        verification = 'true'
    else:
        print("password length was shorter than 7, please try again!")
        verifyPassword()
    return verification

#prints all the user details
def displayAll():
    print('All User Details')
    print('=================')
    myprint(users)
    print('\n Thank you! Goodbye.')

#for more users
def moreUsers():
    print('')
    cont = input('Do you wish to add more users (Y/N): ')
    if cont.lower() == 'y':
        userD.clear()
        userDetails()
    elif cont.lower() == 'n':
        print('\n')
        displayAll()
    else:
        print('invalid input')
        moreUsers()

#display unit user
def displayUserDetails(string):
    feedback = string
    if feedback.lower() == 'y':
        print('Successful.')
        print('User Details')
        print('=================')
        print('First Name: ' + userD[0])
        print('Last Name: ' + userD[1])
        print('Email: ' + userD[2])
        moreUsers()
    elif feedback.lower() == 'n':
        print('Ooops! Soory about that. Would you like to enter your desired Password? (Should be min of 7 characters)')
        verifyPassword()
        print('Successful.')
        print('User Details')
        print('=================')
        print('First Name: ' + userD[0])
        print('Last Name: ' + userD[1])
        print('Email: ' + userD[2])
        moreUsers()
    else:
        check = input("Please enter valid reply (Y / N): ")
        displayUserDetails(check)

#loop through the dictionary
def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print('---------------------')
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))

if __name__ == '__main__':
    userDetails()