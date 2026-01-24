
import services
from bson import ObjectId


class User:

    def __init__(self, userID: str, email: str, name: str, dateOfBirth: str, address: str, password: str):
        self.userID = ObjectId(userID)
        self.email = email
        self.name = name
        self.dob =dateOfBirth
        self.address = address
        self.password = password

    def addNewExpense(self):
        print("\n_____ADDING NEW EXPENSE_____\n")
        return services.createNewExpense(self.userID)

    def seeAllExpenses(self):
        print("\n_____VIEWING ALL EXPENSES_____\n")
        result=services.viewAllExpenses(self.userID)
        return result

    def seeTotalExpense(self):
        print("\n_____VIEWING TOTAL EXPENSES_____\n")
        result = services.viewTotalExpense(self.userID)
        return result

    def userDeleteExp(self, expenseID: str):
        print("\n_____DELETING EXPENSE_____\n")
        result = services.deleteExpense(expenseID)
        return result

    def userExpUpdate(self, expenseID: str, updateChoice: str):
        print("\n_____UPDATING EXPENSE_____\n")
        result = None
        if updateChoice == '1':
            result=services.updateExpDescription(expenseID, updateChoice)
        elif updateChoice == '2':
            result = services.updateExpAmount(expenseID, updateChoice)
        elif updateChoice == '3':
            result = services.updateExpDate(expenseID, updateChoice)
        return result

    def UserSeeAccDetails(self):
        print("\n_____VIEWING ACCOUNT DETAILS_____\n")
        result = services.viewAccDetails(self.userID)
        return result

    def UserUpdateAccDetails(self, accUpdateChoice: str):
        print("\n_____UPDATING ACCOUNT DETAILS_____\n")
        result = None
        if accUpdateChoice == '1':
            result=services.update_accName(self.userID, self.password, accUpdateChoice)
        elif accUpdateChoice == '2':
            result = services.update_accEmail(self.userID, self.password, accUpdateChoice)
        elif accUpdateChoice == '3':
            result = services.update_accDob(self.userID, self.password, accUpdateChoice)
        elif accUpdateChoice == '4':
            result = services.update_accAddress(self.userID, self.password, accUpdateChoice)
        elif accUpdateChoice == '5':
            result = services.update_accPassword(self.userID, self.password, accUpdateChoice)
            passFetch = services.passFetch_connect(self.userID)
            self.password = passFetch['password']
        return result

    def UserDeleteAcc(self):
        print("\n_____DELETING ACCOUNT_____\n")
        result = services.delete_acc(self.userID, self.password)
        return result

    def UserAsksAnalyze(self):
        print("\n_____ANALYZING EXPENSES_____\n")
        analyzeResult = services.analyze_expenses(self.userID)
        return analyzeResult