import sys
sys.path.append("..")
from stock import *

def testPE_ratio(stock):
    print ("Test of P/E Ratio")
    again="YES"
    while again.upper()=="YES":
        marketPrice=float(input("Please enter a market price: "))
        for i in stock:
            print "The P/E ratio for "+i.getStockSymbole()+" is "+str(i.PE_ratio(marketPrice))
        again=""
        while again.upper() not in {"YES","NO"}:
            again=raw_input("Would you like to test P/E ratio again ?(Yes or No): ")
