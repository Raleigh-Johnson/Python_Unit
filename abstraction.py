from abc import ABC,abstractmethod
class car(ABC):
    def paySlip(self,amount):
        print("Your purchase amount: ",amount)
              #Yet to be defined, but ".amount" will be the running counter
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(car):
    def payment(self,amount):
            print('Your purchase amount of {} exeeded your limit of $100'.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
            
    
