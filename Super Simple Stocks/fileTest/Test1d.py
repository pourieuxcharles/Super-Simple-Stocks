import sys
sys.path.append("..")
from stock import *
import random

def testDividendYield(stock):
    test=True

    # create random marketPrices
    marketPrices=[]
    for i in range(20):
        marketPrices.append(random.random()*10000000)
    for marketPrice in marketPrices:

        if stock[0].dividend_yield(marketPrice)!=0 and stock[1].dividend_yield(marketPrice)!=8.00/marketPrice and stock[2].dividend_yield(marketPrice)!=23.00/marketPrice and stock[3].dividend_yield(marketPrice)!=0200*100/marketPrice and stock[4].dividend_yield(marketPrice)!=13.00/marketPrice:
            print "Error on the calculation test"            
            test=False

    #test for a market price not as a number
    marketPrice="m"
    for st in stock:
        if st.dividend_yield(marketPrice)!="market price is not a positive number":
            print "Error on marketPrice not a positive number test" 
            test=False
    return test
