import sys
sys.path.append("..")
from stock import *
from GBCE import *
import datetime
import math
import random

def testGBCE(stock):
    test=True

    if math.pow(stock[0].volumeWeightedStockPrice()*stock[1].volumeWeightedStockPrice()*stock[2].volumeWeightedStockPrice(),1.0/3)!=GBCE(stock):
	    test=False

    for i in stock:
        i.setTrades([])

    stock[0].add_trade(datetime.datetime.now(),10,"buy",10)

    if math.pow(stock[0].volumeWeightedStockPrice(),1.0/1)!=GBCE(stock):
	    test=False

    stock[0].add_trade(datetime.datetime.now(),56,"sell",24.24)

    if math.pow(stock[0].volumeWeightedStockPrice(),1.0/1)!=GBCE(stock):
	    test=False

    for i in stock:
        if stock.index(i)%2==0:
            i.add_trade(datetime.datetime.now(),random.random()*1000000,"buy",random.random()*1000000)
        else:
            i.add_trade(datetime.datetime.now(),random.random()*1000000,"sell",random.random()*1000000)

    if math.pow(stock[0].volumeWeightedStockPrice()*stock[1].volumeWeightedStockPrice()*stock[2].volumeWeightedStockPrice()*stock[3].volumeWeightedStockPrice()*stock[4].volumeWeightedStockPrice(),1.0/5)!=GBCE(stock):
	    test=False

    for i in stock:
        if stock.index(i)%2!=0:
            i.add_trade(datetime.datetime.now(),(stock.index(i)+1)*2,"buy",random.random()*1000000)
        else:
            i.add_trade(datetime.datetime.now(),(stock.index(i)+1)*3,"sell",random.random()*1000000)

    if math.pow(stock[0].volumeWeightedStockPrice()*stock[1].volumeWeightedStockPrice()*stock[2].volumeWeightedStockPrice()*stock[3].volumeWeightedStockPrice()*stock[4].volumeWeightedStockPrice(),1.0/5)!=GBCE(stock):
	    test=False
    return test
