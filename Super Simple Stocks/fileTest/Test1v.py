import sys
sys.path.append("..")
from stock import *
import datetime

def testVolumeWeightedStockPrice(stock):

    for i in stock:
        i.setTrades([]) #empties trades

    test=True
    for i in stock:
        if i.volumeWeightedStockPrice()!="No trade for "+i.getStockSymbole():
            print "error on the no trade test"
            test=False #test empty response for trades for all stocks

    for i in stock:
        if i.getStockSymbole()=="TEA" or i.getStockSymbole()=="GIN":
            i.add_trade("2017-01-20 01:54:14", 10, "buy", 1.5) #add a value to GIN and TEA that should not be consider (before the last 15 minutes)
            i.add_trade("2016-04-02 15:01:47", 54, "sell", 124.87) #add a value to GIN and TEA that should not be consider (before the last 15 minutes)
        elif i.getStockSymbole()=="POP" or i.getStockSymbole()=="ALE":
            i.add_trade(datetime.datetime.now()-datetime.timedelta(minutes=5), 57, "sell", 64.12) #add a value to POP and ALE that should be consider in the calculation 

    for i in stock:
        if (i.getStockSymbole()=="TEA" or i.getStockSymbole()=="GIN") and i.volumeWeightedStockPrice()!="No trade match the criterias "+i.getStockSymbole(): 
            print "Error on the No trade match the criterias test"          
            test=False
        elif (i.getStockSymbole()=="POP" or i.getStockSymbole()=="ALE") and i.volumeWeightedStockPrice()!=64.12*57/57:
            print "Error on the 1 trade test"
            test=False

    for i in stock:
        if i.getStockSymbole()=="GIN":
            i.add_trade("2001-08-12 01:54:14", 10, "buy", 1.5) #add a value to GIN  that should not be consider (before the last 15 minutes)
            i.add_trade("1999-11-30 15:01:47", 14, "sell", 0.87) #add a value to GIN that should not be consider (before the last 15 minutes)
        elif i.getStockSymbole()=="TEA":
            i.add_trade(datetime.datetime.now()-datetime.timedelta(minutes=1), 73, "buy", 1.5)
        elif i.getStockSymbole()=="POP":
            i.add_trade(datetime.datetime.now()-datetime.timedelta(minutes=16), 505, "buy", 101.25) #add POP that should not be consider in the calculation
        elif i.getStockSymbole()=="ALE":
            i.add_trade(datetime.datetime.now()-datetime.timedelta(minutes=14), 42, "buy", 109) #add ALE that should be consider in the calculation 
             


    for i in stock:
        if i.getStockSymbole()=="GIN" and i.volumeWeightedStockPrice()!="No trade match the criterias "+i.getStockSymbole():
            print "Error 4 not consider"     
            test=False
        elif i.getStockSymbole()=="TEA" and i.volumeWeightedStockPrice()!=73*1.5/73:
            print "Error 1 not consider and 1 consider"
            test=False
        elif i.getStockSymbole()=="POP" and i.volumeWeightedStockPrice()!=64.12*57/57:
            print "Error 1 consider and 1 not consider"
            test=False

        elif i.getStockSymbole()=="ALE" and i.volumeWeightedStockPrice()!=(64.12*57+42*109)/(57+42):
            print "Error 2 consider with 1 buy and 1 sell"
            test=False
        return test

