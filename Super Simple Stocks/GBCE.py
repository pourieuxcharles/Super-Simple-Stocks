from stock import *
import math

def GBCE(stock):
    gbceCal=1
    tradeNum=0
    for st in stock:
        if type(st.volumeWeightedStockPrice())==int or type(st.volumeWeightedStockPrice())==float:
            gbceCal*=st.volumeWeightedStockPrice()
            tradeNum+=1
    try:
        return math.pow(gbceCal,1.0/tradeNum)
    except ZeroDivisionError:
        print "No market price"
        return False
