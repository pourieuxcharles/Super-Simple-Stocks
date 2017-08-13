import sys
sys.path.append("..")
from stock import *
from GBCE import *
import datetime
import math
import random

def testGBCE(stock):
    test=True

#test with the trade from the previous test TEA, POP and ALE use volume Weighted Stock Price GIN use the last known trade and JOE is empty    
    if math.pow(stock[0].volumeWeightedStockPrice()*stock[1].volumeWeightedStockPrice()*stock[2].volumeWeightedStockPrice()*stock[3].getLastTradePrice(),1.0/4)!=GBCE(stock):
        test=False

#test with no trade should return false
    for i in stock:
        i.setTrades([])

    if GBCE(stock)!=False:
        test=False

#test with only 1 trade
    stock[0].add_trade(datetime.datetime.now(),10,"buy",10)

    if math.pow(stock[0].volumeWeightedStockPrice(),1.0/1)!=GBCE(stock):
	    test=False

#test with only 2 trade on TEA others empties
    stock[0].add_trade(datetime.datetime.now(),56,"sell",24.24)

    if math.pow(stock[0].volumeWeightedStockPrice(),1.0/1)!=GBCE(stock):
	    test=False

#add trades to all stock
    for i in stock:
        if stock.index(i)%2==0:
            i.add_trade(datetime.datetime.now(),random.random()*1000000,"buy",random.random()*1000000)
        else:
            i.add_trade(datetime.datetime.now(),random.random()*1000000,"sell",random.random()*1000000)

    if math.pow(stock[0].volumeWeightedStockPrice()*stock[1].volumeWeightedStockPrice()*stock[2].volumeWeightedStockPrice()*stock[3].volumeWeightedStockPrice()*stock[4].volumeWeightedStockPrice(),1.0/5)!=GBCE(stock):
	    test=False

#add other trade to all stock
    for i in stock:
        if stock.index(i)%2!=0:
            i.add_trade(datetime.datetime.now(),(stock.index(i)+1)*2,"buy",random.random()*1000000)
        else:
            i.add_trade(datetime.datetime.now(),(stock.index(i)+1)*3,"sell",random.random()*1000000)

    if math.pow(stock[0].volumeWeightedStockPrice()*stock[1].volumeWeightedStockPrice()*stock[2].volumeWeightedStockPrice()*stock[3].volumeWeightedStockPrice()*stock[4].volumeWeightedStockPrice(),1.0/5)!=GBCE(stock):
	    test=False 
    return test
