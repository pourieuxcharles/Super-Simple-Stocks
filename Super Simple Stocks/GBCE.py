from stock import *
import math

#get all

def GBCE(stock):
    gbceCal=1
    tradeNum=0
    for st in stock:
        # Use volume Weighted Stock Price if possible
        if type(st.volumeWeightedStockPrice())==int or type(st.volumeWeightedStockPrice())==float:
            gbceCal*=st.volumeWeightedStockPrice()
            tradeNum+=1
        # Otherwise use the last price known
        elif st.getLastTradePrice()!=False:
            gbceCal*=st.getLastTradePrice()
            tradeNum+=1
    try:
        return math.pow(gbceCal,1.0/tradeNum)
    except ZeroDivisionError:
        print "No market price"
        return False
