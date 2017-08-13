import sys
sys.path.append("..")
from stock import *

def testDividendYield(stock):
    print ("Test of dividend yield")
    again="YES"
    while again.upper()=="YES":
        marketPrice=float(input("Please enter a market price: "))
        for i in stock:
            print "The dividend yield for "+i.getStockSymbole()+" is "+str(i.dividend_yield(marketPrice))
        again=""
        while again.upper() not in {"YES","NO"}:
            again=raw_input("Would you like to test dividend yield again ?(Yes or No): ")
