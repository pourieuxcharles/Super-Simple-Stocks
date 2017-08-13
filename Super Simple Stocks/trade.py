
class Trade():
    def __init__(self,timestamp,quantity,b_s,price):
		self.__timestamp=timestamp
		self.__quantity=quantity
		self.__b_s=b_s
		self.__price=price

    def getTimestamp(self):
        return self.__timestamp

    def setTimestamp(self,timestamp):
        self.__timestamp=timestamp
    
    def getQuantity(self):
        return self.__quantity

    def setQuantity(self,quantity):
        self.__quantity=quantity

    def getB_s(self):
        return self.__b_s

    def setB_s(self,b_s):
        self.__b_s=b_s

    def getPrice(self):
        return self.__price

    def setPrice(self,price):
        self.__price=price

    def printTrade(self):
        print str(self.getTimestamp())+" "+str(self.getQuantity())+" "+str(self.getB_s())+" "+str(self.getPrice())
