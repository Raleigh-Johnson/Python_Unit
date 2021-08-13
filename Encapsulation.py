class Protected: #Main class
    def __init__(self):
        self._protectedVar = 12
# Private Variable
    def getPrivate(self):
        print(self.__privateVar)
#setting a number as private
    def setPrivate(self,private):
        self.__privateVar = private
        print(private)
obj = Protected()
obj.setPrivate(23)
obj.getPrivate()
