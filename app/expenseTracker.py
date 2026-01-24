
import services
from sys import exit
from user import User
import utils

class ExpenseTracker:

    def startMenu(self):
        options: list = ['0', '1', '2']
        while True:
            print("\n=====PERSONAL EXPENSE TRACKER=====")
            print("Enter 1 to sign up.\nEnter 2 to log in.\nEnter 0 to exit")
            choice: str = input("Enter your choice: ")
            if choice in options:
                if choice == '1':
                    self.signUp()
                elif choice == '2':
                    self.login()
                elif choice == '0':
                    exit("Have a nice day! Bye...")
            else:
                print("Invalid input. Please try again. <Start Menu>")

    def signUp(self):                                   #Name, email, date of birth, address, password
        print("\n_____Sign Up Session_____\n")
        name = input("Enter name: ")
        email = input("Enter email: ")
        dob = input("Enter date of birth: ")
        address = input("Enter address: ")
        password = input("Enter password: ")
        #Name
        name: str = input("Enter name: ").strip().lower()
        #Email
        while True:
            email: str = input("Enter email: ").strip()
            emailCheck:bool = utils.emailValidator(email)
            if not emailCheck:
                print("Invalid Email. Try again...<Sign up email>")
                continue
            break
        #Date of Birth
        while True:
            dob: str = input("Enter date of birth (DD-MM-YY): ").strip()
            dobCheck: bool = utils.dobValidator(dob)
            if not dobCheck:
                print("Invalid date of birth...<Sign up dob>")
                continue
            break
        #Address
        address: str = input("Enter address: ")
        #Password
        while True:
            password: str = input("Enter password: ")
            passCheck: bool = utils.passwordStrength(password)
            if not password:
                print("Weak password...<Sign up password>")
                continue
            break
        signUp_result = services.signUpConnector(name, email, dob, address, password)
        if not signUp_result:
            print("SIGN UP FAILED...<Sign up session>")
        else:
            print("SUCCESSFULLY SIGNED UP")

    def login(self):
        print("\n_____Login Session_____\n")
        email: str = input("Enter email: ")
        password: str = input("Enter password: ")
        login_result=services.loginConnector(email, password)
        if not login_result: # ----> Being 'None'
            print("USER NOT FOUND<log in session>...")
        else:
            print(f"\n_____WELCOME {login_result['name'].upper()}_____\n")
            userID: str = login_result['_id']
            email: str = login_result['email']
            name: str = login_result['name']
            dateOfBirth: str = login_result['dateOfBirth']
            address: str = login_result['address']
            password: str = login_result['password']
            self.loginMenu(userID, email, name, dateOfBirth, address, password)

    def loginMenu(self, userID: str, email: str, name: str, dateofBirth: str, address: str, password: str):
        user = User(userID, email, name, dateofBirth, address, password)        #---> User object creation
        while True:
            print("Enter 1 to add new expense.\nEnter 2 to view all expenses.\nEnter 3 to view total expense.\n"
                  "Enter 4 to delete an expense.\nEnter 5 to update expense details.\nEnter 6 to view account details.\n"
                  "Enter 7 to update account details.\nEnter 8 to delete account.\nEnter 9 to analyze expense record.\n"
                  "Enter 0 to log out.")
            userChoice: str = input("Enter here: ")
            if userChoice.isdigit() and 0<=int(userChoice)<=9:
                if userChoice=='1':
                    l_menu_addingNewexpense(user)
                elif userChoice=='2':
                    l_menu_viewAllExps(user)
                elif userChoice=='3':
                    l_menu_viewTotalExps(user)
                elif userChoice=='4':
                    l_menu_deleteExp(user)
                elif userChoice=='5':
                    l_menu_updateExp(user)
                elif userChoice=='6':
                    l_menu_viewAccDetail(user)
                elif userChoice=='7':
                    l_menu_updateAccDetails(user)
                elif userChoice=='8':
                    result = l_menu_deleteAcc(user)
                    if result is None:
                        continue
                    else:
                        break
                elif userChoice=='9':
                    l_menu_analyze(user)
                elif userChoice=='0':
                    break
            else:
                print("Invalid choice. Try again...<log-in Menu>\n")

def l_menu_addingNewexpense(user: User):
    result = user.addNewExpense()
    if not result:
        print("ADDING EXPENSE FAILED...<l_menu_addingNewexpense>\n")
    else:
        print("NEW EXPENSES ADDED!\n")

def l_menu_viewAllExps(user: User):
    result = user.seeAllExpenses()
    if not result:
        print("NO EXPENSE DATA FOUND...<l_menu_addingNewexpense>\n")
    else:
        for expense in result:
            ID = expense['_id']
            description = expense['description']
            amount = expense['amount']
            date = expense['date']
            print(f"ID:{ID}, description: {description}, amount: {amount}, date: {date}")
        print('\n')

def l_menu_viewTotalExps(user: User):
    total = 0.0
    result = user.seeTotalExpense()
    if not result:
        print("NO EXPENSE DATA YET...<l_menu_viewTotalExps>\n")
    else:
        for expense in result:
            total += expense['amount']
        print(f"TOTAL AMOUNT = {total}\n")

def l_menu_deleteExp(user: User):
    print("\nNOTE>>You need to enter ID of the expense you want to delete.")
    expenseID: str = input('Enter expense ID to delete: ')
    lastChance: str = input("Are you sure?\nIf you are, press 1. Otherwise, press 0.\nEnter here: ")
    if lastChance=='0':
        print("DELETING EXPENSE CANCELLED...\n")
    elif lastChance=='1':
        result=user.userDeleteExp(expenseID)
        if result is None:
            print("DELETING EXPENSE FAILED...<l_menu_deleteExp>\n")
        elif result == 0:
            print("NO MATCHED EXPENSE DATA...<l_menu_deleteExp>\n")
        elif result == 1:
            print("EXPENSE DELETED.\n")
    else:
        print(f"Invalid input. Try again...<l_menu_deleteExp>\n")

def l_menu_updateExp(user: User):
    print("\nNote>>You need to enter ID of the expense you want to update.")
    expenseID: str = input("Enter expense ID to update: ")
    while True:
        expUpdateChoice : str = input("Enter 1 to update description.\nEnter 2 to update amount.\nEnter 3 to update date.\n"
                                      "Enter here: ")
        if expUpdateChoice.isdigit() and 1<=int(expUpdateChoice)<=3:
            result = user.userExpUpdate(expenseID, expUpdateChoice)
            if result is None:
                print("NO EXPENSE WAS UPDATED...<l_menu_updateExp>\n")
            else:
                print("EXPENSE DATA UPDATED.\n")
            break

        else:
            print("Invalid input. Try again...<l_menu_updateExp>\n")

def l_menu_viewAccDetail(user: User):
    result = user.UserSeeAccDetails()
    if not result:
        print("NO EXPENSE DATA FOUND...<l_menu_viewAccDetail>\n")
    else:
        Name = result['name']
        Email = result['email']
        Dob = result ['dateOfBirth']
        Address = result ['address']
        print(f'Name: {Name}, Email: {Email}, Date of Birth: {Dob}, Address: {Address}\n')

def l_menu_updateAccDetails(user: User):
    print("\nNote>>>You will need to enter password to change your account details.")
    while True:
        accUpdateChoice : str = input("Enter 1 to update name.\nEnter 2 to update email.\nEnter 3 to update date of birth\n"
                                      "Enter 4 to update address.\nEnter 5 to update password.\nEnter here: ")
        if accUpdateChoice.isdigit() and 1<=int(accUpdateChoice)<=5:
            #print("GOOD")                          #delete later
            result = user.UserUpdateAccDetails(accUpdateChoice)
            print(f"RESULT = {result}")
            if result is None:
                print("NO DETAILS WERE UPDATED...<l_menu_updateExp>\n")
            else:
                print("ACCOUNT DETAIL UPDATED.\n")
            break
        else:
            print("Invalid Input. Try again...<l_menu_updateAccDetails>\n")

def l_menu_deleteAcc(user: User):
    print("\nNOTE>>>You will need to enter password to delete your account.\n"
          "ALL THE INFORMATION WILL BE LOST!")
    result = user.UserDeleteAcc()
    if result is None:
        print("DELETING ACC FAILED...<l_menu_deleteAcc>\n")
        return None
    else:
        print("ACC DELETED.\n")
        return result

def l_menu_analyze(user: User):
    result: int=user.UserAsksAnalyze()
    if result == -1:
        print("⚠️ Your expenses are more than 50% of your salary. This is BAD.\n")
    elif result == 1:
        print("✅ Your expenses are within a healthy range.\n")