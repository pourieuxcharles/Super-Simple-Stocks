import sys
sys.path.append("..")
from stock import *

def testDividendYield(stock):
    marketPrices={1.1,2.20,0.65,92.8,5,10,1000}
    test=True
    for marketPrice in marketPrices:

        if stock[0].dividend_yield(marketPrice)!=0 and stock[1].dividend_yield(marketPrice)!=8.00/marketPrice and stock[2].dividend_yield(marketPrice)!=23.00/marketPrice and stock[3].dividend_yield(marketPrice)!=0200*100/marketPrice and stock[4].dividend_yield(marketPrice)!=13.00/marketPrice:
            print "Error on the calculation test"            
            test=False
    marketPrice="m"
    for st in stock:
        if st.dividend_yield(marketPrice)!="market price is not a positive number":
            print "Error on marketPrice not a positive number test" 
            test=False
    return test
