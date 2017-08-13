import sys
sys.path.append("..")
from stock import *
import random

def testPERatio(stock):
    test=True

    # create random values for market price
    marketPrices=[]
    for i in range(20):
        marketPrices.append(random.random()*10000000)
    
    for marketPrice in marketPrices:
        if stock[0].PE_ratio(marketPrice)!="Can't be calculed division by zero" and stock[1].PE_ratio(marketPrice)!=marketPrice/stock[1].dividend_yield(marketPrice) and stock[2].PE_ratio(marketPrice)!=marketPrice/stock[2].dividend_yield(marketPrice) and stock[3].PE_ratio(marketPrice)!=marketPrice/stock[3].dividend_yield(marketPrice) and stock[4].PE_ratio(marketPrice)!=marketPrice/stock[4].dividend_yield(marketPrice):
            print "Error on the calculation test"            
            test=False
    
    #test for market price not as a number
    marketPrice="m"
    for st in stock:
        if st.dividend_yield(marketPrice)!="market price is not a positive number":
            print "Error on marketPrice not a positive number test"
            test=False
    return test
