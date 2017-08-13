import sys
sys.path.append("..")
from stock import *
from getIndex import *
import datetime

def checkFormatDate():
    while True:
        try:
            timestamp=raw_input("Please enter a timestamp with the format YYYY-MM-DD HH:MM:SS:")
            timestamp=datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            break
        except ValueError:
            print "Please check the format and if the date/time is accurate"
    return timestamp

def getDate():
    #timestamp=checkFormatDate()
    timestamp=raw_input("Please enter a timestamp with the format YYYY-MM-DD HH:MM:SS:")
    """while timestamp>datetime.datetime.now():
        print "Please enter a date previous as the actual date"
        timestamp=checkFormatDate()"""
    return timestamp

def getTrade(stock):
    stockSymbole=""
    while stockSymbole.upper() not in {"TEA", "POP", "ALE", "GIN", "JOE"}:
        stockSymbole = raw_input("Please enter a stock symbole: ")
    timestamp=getDate()
    while True:
        try:			
            quantity= int(input("Please enter a quantity: "))
            break
        except NameError:
            print "Please entrer a number"
		
    b_s=""    
    while b_s not in {"BUY", "SELL"}:
        b_s = raw_input("Please enter a buy or sell: ")
        b_s=b_s.upper()
	  
    while True:	
        try:			
            price= float(input("Please enter a price: "))
            break
        except NameError:
            print "Please entrer a number"
    stock[getIndex(stockSymbole.upper(),stock)].add_trade(timestamp, quantity,b_s,price)





def testAddTrade(stock):
    print ("Test of adding trades")
    again="YES"
    while again.upper()=="YES":
        getTrade(stock)
        again=""
        while again.upper() not in {"YES","NO"}:
            again=raw_input("Do you want to add more trade? (Please enter Yes or No): ")
