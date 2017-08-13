from trade import *
from testType import *
import datetime
class Stock:
    
    def __init__(self,stockSymbole,stockType,lastDividend,fixedDividend,perValue):
        self.__stockSymbole=stockSymbole
        self.__stockType=stockType
        self.__lastDividend=lastDividend
        self.__fixedDividend=fixedDividend
        self.__perValue=perValue
        self.__trades=[]

    def getStockSymbole(self):
        return self.__stockSymbole

    def setStockSymbole(self,stockSymbole):
        self.__stockSymbole=stockSymbole

    def getStockType(self):
        return self.__stockType

    def setStockType(self,stockType):
        self.__stockType=stockType

    def getLastDividend(self):
        return self.__lastDividend

    def setLastDividend(self,lastDividend):
        self.__lastDividend=lastDividend

    def getFixedDividend(self):
        return self.__fixedDividend

    def setFixedDividend(self,fixedDividend):
        self.__fixedDividend=fixedDividend

    def getPerValue(self):
        return self.__perValue

    def setPerValue(self,perValue):
        self.__perValue=perValue

    def getTrades(self):
        return self.__trades

    def setTrades(self,trades):
        self.__trades=trades


    def printAllTrades(self):
        for trade in self.getTrades():
            trade.printTrade()

    def dividend_yield(self,marketPrice):
        if isNumber(marketPrice):
            if self.getStockType()=="Preferred":
                return self.getFixedDividend()*self.getPerValue()/marketPrice
            else:
                return self.getLastDividend()/marketPrice
        else:
            return "market price is not a positive number"
	
    def PE_ratio(self,marketPrice):
        if isNumber(marketPrice):
            if self.dividend_yield(marketPrice)==0:
                return "Can't be calculed division by zero"
            else:
                return marketPrice/self.dividend_yield(marketPrice)
        else:
            return "market price is not a positive number"
    
		
    def add_trade(self,timestamp, quantity,b_s,price):
        if type(timestamp)!=datetime.datetime:        
            timestamp=testTimestamp(timestamp)
        if isNumber(quantity) and isNumber(price) and timestamp!="Please check the format and if the date/time is accurate" and testDatePast(timestamp) and sellOrBuy(b_s):
            print "The trade as been added"
            self.__trades.append(Trade(timestamp, quantity,b_s.upper(),price))
            return True
        else:
            print "Please check information"
            return False

    def volumeWeightedStockPrice(self):
        sumQuantity=0
        sumPriQuan=0
        comptUsed=0
        for trade in self.getTrades():
            if trade.getTimestamp()-datetime.datetime.now()<datetime.timedelta(minutes=15) and trade.getTimestamp()-datetime.datetime.now()>datetime.timedelta(minutes=-15):
                sumPriQuan+=(trade.getPrice()*trade.getQuantity())
                comptUsed+=1
                sumQuantity+=trade.getQuantity()
        if len(self.getTrades())==0:
            return "No trade for "+self.getStockSymbole()
        elif comptUsed==0:
            return "No trade match the criterias "+self.getStockSymbole()        
        elif sumQuantity==0:
            return "No quantity for "+self.getStockSymbole()
        else:
            return sumPriQuan/sumQuantity     	
