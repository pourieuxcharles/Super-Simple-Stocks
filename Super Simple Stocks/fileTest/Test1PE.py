import sys
sys.path.append("..")
from stock import *

def testPERatio(stock):
    marketPrices={1.1,2.20,0.65,92.8,5,10,1000}
    test=True
    for marketPrice in marketPrices:

        if stock[0].PE_ratio(marketPrice)!="Can't be calculed division by zero" and stock[1].PE_ratio(marketPrice)!=marketPrice/stock[1].dividend_yield(marketPrice) and stock[2].PE_ratio(marketPrice)!=marketPrice/stock[2].dividend_yield(marketPrice) and stock[3].PE_ratio(marketPrice)!=marketPrice/stock[3].dividend_yield(marketPrice) and stock[4].PE_ratio(marketPrice)!=marketPrice/stock[4].dividend_yield(marketPrice):
            print "Error on the calculation test"            
            test=False
    marketPrice="m"
    for st in stock:
        if st.dividend_yield(marketPrice)!="market price is not a positive number":
            print "Error on marketPrice not a positive number test"
            test=False
    return test
