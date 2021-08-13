class Protected:
    def __init__(self):
        self._protectedVar = 12

    def getPrivate(self):
        print(self.__privateVar)
    
    def setPrivate(self,private):
        self.__privateVar = private

obj = Protected()
obj.setPrivate(23)
obj.getPrivate()
