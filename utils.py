import string
from ctypes import c_uint16
from xmlrpc.client import FastParser


from re import match
from datetime import datetime
from string import punctuation

def salary_validator(salary: float):
    if salary <= 0 :
        return False
    else:
        return True

def dateValidator(date: str) -> bool:
    #DD-MM-YY
    daysOfMonths = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    try:
        dobList: list = date.split('-')
        #Year
        year = int(dobList[2])
        currentYear = datetime.now().year
        if year>currentYear:
            return False
        #Month
        month = int(dobList[1])
        currentMonth = datetime.now().month
        if month >12:
            return False
        elif month>currentMonth:
            if year == currentYear:
                return False
        #Day
        day = int(dobList[0])
        currentDay = datetime.now().day
        #leap year check
        if day == 29 and month == 2:
            leapYearCheck = year % 4
            if leapYearCheck!=0:
                return False
        elif day>daysOfMonths[month]:
            return False
        elif day>currentDay:
            if month==currentMonth and year==currentYear:
                return False
        return True
    except ValueError as e:
        return False
    except Exception as e:
        return False

def amountValidator(amount: float):
    """
    :param amount:
    :return:>bool
    Amount cannot be zero or negative.
    if invalid amount -> False
    if valid amount -> True
    """
    if amount <= 0:
        return False
    else:
        return True

def passwordStrength(password: str):
    """
    :param password:
    :return:>Boolean
    This function will be responsible in qualifying the strength of a password.
    Strong password -> True
    Weak password -> False
    """
    digit_count = 0
    specialChar_count = 0
    for char in password:
        if char in punctuation: #---> from string module
            specialChar_count+=1
    for char in password:
        if char.isdigit():
            digit_count+=1
    if digit_count>=2 and specialChar_count>=2:
        return True
    else:
        return False

def emailValidator(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    result = match(pattern, email)
    if result:
        return True
    else:
        return False

def dobValidator(dob: str) -> bool:
    # DD-MM-YY
    daysOfMonths = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    try:
        dobList: list = dob.split('-')
        year = int(dobList[2])
        currentYear = datetime.now().year
        yearGap = currentYear-year
        if yearGap <= 10:
            return False
        month = int(dobList[1])
        if month >12:
            return False
        day = int(dobList[0])
        if day>daysOfMonths[month]:
            return False
        return True
    except ValueError as e:
        return False
    except Exception as e:
        return False