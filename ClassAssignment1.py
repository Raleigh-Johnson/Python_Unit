#Python 3.9.5
# Author Raleigh J.
# Created on 8/9/21
class User:
    name = "No name provided"
    email = ""
    password = "1234abcd"
    accountNum = 0

class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ''
    mailing_list = True
