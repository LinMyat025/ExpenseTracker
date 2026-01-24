"""
This module w
"""
from pprint import pprint

from db import userDB, expenseDB
from utils import utils


def loginConnector(email: str, password: str):
    userData = {'email': email, 'password': password}
    return userDB.userRead(userData)

def signUpConnector(name: str, email: str, dob: str, address: str, password: str):
    userData = {'name': name, 'email': email, 'dateOfBirth': dob, 'address':address, 'password': password}
    return userDB.userCreate(userData)

def createNewExpense(userID):
    #userID ---> type=ObjectID
    expenseData = {}
    description: str = input("Enter expense description: ")
    while True:
        try:
            amount: float = float(input("Enter amount: "))
            result: bool = utils.amountValidator(amount)
            if not result:
                print("Invalid amount. Try again...<createNewExpense>")
                continue
            break
        except ValueError as e:
            print(f"Invalid input. Try again...{e}")
    while True:
        spentDate: str = input("Enter date (DD-MM-YY): ")
        result: bool = utils.dateValidator(spentDate)
        if not result:
            print("Invalid date. Try again...<createNewExpense>")
            continue
        break
    expenseData.update({'description':description, 'amount': amount, 'date':spentDate, 'userID':userID})
    result: bool = expenseDB.expenseCreate(expenseData)
    return result

def viewAllExpenses(userID):
    #userID ---> type=ObjectID
    result=expenseDB.expenseRead(userID)
    return result

def viewTotalExpense(userID):
    #userID ---> type=ObjectID
    result = expenseDB.expenseRead(userID)
    return result

def deleteExpense(expenseID: str):
    #expenseID ---> type = str
    result = expenseDB.expenseDelete(expenseID)
    return result

def updateExpDescription(expenseID: str, updateChoice: str):
    #expenseID ---> type = str
    data = input("Enter new description: ")
    result = expenseDB.expUpdate(expenseID, updateChoice, data)
    return result

def updateExpAmount(expenseID: str, updateChoice: str):
    #expenseID ---> type = str
    while True:
        data = input("Enter new amount: ")
        if data.isdigit():
            result = expenseDB.expUpdate(expenseID, updateChoice, data)
            break
        else:
            print("Only enter digits...<services.updateExpAmount>")
    return result

def updateExpDate(expenseID: str, updateChoice: str):
    #expenseID ----> type = str
    while True:
        data = input("Enter new data (DD-MM-YY): ")
        if utils.dateValidator(data):
            result = expenseDB.expUpdate(expenseID, updateChoice, data)
            break
        else:
            print("Invalid Date. Try again...<services.updateExpDate>")
    return result

def viewAccDetails(userID):
    #userID ----> type = ObjectID
    userID_dict = {'_id': userID}
    result = userDB.AccDetailRead(userID_dict)
    return result

def update_accName(userID, password: str, accUpdateChoice: str):
    # userID ----> type = ObjectID
    newName  = input("Enter new name: ")
    passCheck = input("Enter password to update: ")
    #print(password)                                        #delete later
    #print(type(password))                                  #delete later
    if passCheck != password:
        print("Incorrect Password...<update_accName>")
        return None
    else:
        result = userDB.AccDetailUpdate(userID, accUpdateChoice, newName)
        return result

def update_accEmail(userID, password: str, accUpdateChoice: str):
    # userID ----> type = ObjectID
    while True:
        newEmail = input("Enter new email: ")
        emailCheck: bool= utils.emailValidator(newEmail)
        if not emailCheck:
            print("Invalid Email. Try again...<update_accEmail>")
        else:
            break
    passCheck = input("Enter password to update: ")
    if passCheck != password:
        print("Incorrect Password...<update_accEmail>")
        return None
    else:
        result = userDB.AccDetailUpdate(userID, accUpdateChoice, newEmail)
        return result

def update_accDob(userID, password: str, accUpdateChoice: str):
    # userID ----> type = ObjectID
    while True:
        newDob = input("Enter new date of birth: ")
        dobCheck: bool = utils.dobValidator(newDob)
        if not dobCheck:
            print("Invalid date of birth. Try again...<update_accDob>")
        else:
            break
    passCheck = input("Enter password to update: ")
    if passCheck != password:
        print("Incorrect Password...<update_accDob>")
        return None
    else:
        result = userDB.AccDetailUpdate(userID, accUpdateChoice, newDob)
        return result

def update_accAddress(userID, password: str, accUpdateChoice: str):
    # userID ----> type = ObjectID
    newAddress = input("Enter new address: ")
    passCheck = input("Enter password to update: ")
    if passCheck != password:
        print("Incorrect Password...<update_accAddress>")
        return None
    else:
        result = userDB.AccDetailUpdate(userID, accUpdateChoice, newAddress)
        return result

def update_accPassword(userID, password: str, accUpdateChoice: str):
    # userID ----> type = ObjectID
    newPassword1 = input("Enter new password: ")                    #delete later
    # while True:
    #     newPassword1 = input("Enter new password: ")
    #     newPass_quality: bool = utils.passwordStrength(newPassword1)
    #     if not newPass_quality:
    #         print("Weak password...<update_accPassword>")
    #     else:
    #         newPassword2 = input("Enter new password again: ")
    #         if newPassword1 != newPassword2:
    #             print("Password not the same...<update_accPassword")
    #         else:
    #             break
    passCheck = input("Enter current password to update: ")
    if passCheck == password:
        result = userDB.AccDetailUpdate(userID, accUpdateChoice, newPassword1)
        return result
    else:
        print("Incorrect password. Try again...<update_accPassword>")
        return None

def delete_acc(userID, password: str):
    # userID ----> type = ObjectID
    while True:
        lastChance = input("Are you sure to delete your acc?\nEnter 1 to proceed."
                           "\nEnter 0 to cancel.")
        if lastChance.isdigit() and (lastChance == '0' or lastChance=='1'):
            if lastChance=='0':
                return None
            elif lastChance == '1':
                passCheck = input("Enter password to delete acc: ")
                if passCheck != password:
                    print("Incorrect password...<delete_acc>")
                    return None
                else:
                    result = userDB.AccDelete(userID)
                    return result
        else:
            print("Invalid Input. Try again...<delete_acc>")
            continue

def analyze_expenses(userID):
    # userID ---> type = ObjectID
    totalExp = 0.0
    while True:
        salary = input("Enter your monthly salary: ")
        try:
            salary = float(salary)
            salaryCheck: bool = utils.salary_validator(salary)
            if not salaryCheck:
                print("Salary must not be negative or zero.")
                continue
            break
        except ValueError:
            print("Invalid Input. Try again...<analyze-expenses>")
    half_salary = salary/2
    totalExpList: list = viewTotalExpense(userID)
    #pprint(totalExpList)
    for i in totalExpList:
        totalExp+=i['amount']
    if totalExp>=half_salary:
        return -1
    else:
        return 1

def passFetch_connect(userID):
    passFetch = userDB.passFetcher(userID)
    return passFetch


