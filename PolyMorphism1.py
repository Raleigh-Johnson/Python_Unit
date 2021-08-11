class User: 
    name = "Jeff"
    email = "JeffW@gmail.com"
    password = "123abc"
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is inorrect.")
        
# Child class 1
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your password: ")
        if (entry_email == self.email and entry_pin -- self.pin_number)
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")


class Manager(User):
    base_pay = 15.00
    department = "Management"
    pin_number = "0451"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your password: ")
        if (entry_email == self.email and entry_pin -- self.pin_number)
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
