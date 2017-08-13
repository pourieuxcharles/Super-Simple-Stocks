import sys
sys.path.append("..")
from stock import *
import datetime

def testAddTrades(stock):
    test=True
    for i in stock:
        test2=i.add_trade("2017-08-10 00:00:00",10,"buy",0.025)#expected added
        if test2==False:
            print "Error on the expected added test"
            test=False

    for i in stock:
        test2=i.add_trade(str(datetime.datetime.now()+datetime.timedelta(minutes=15)),10,"buy",0.025)#expected not added - Timestamp in the futur
        if test2==True:
            test=False

    for i in stock:
        test2=i.add_trade("2017-08-10",10,"buy",0.025)#expected not added - Timestamp format
        if test2==True:
            print "Error on the timestamp format error test"
            test=False

    for i in stock:
        test2=i.add_trade("2017-08-10 00:00:00","m","buy",0.025)#expected not added - Quantity format
        if test2==True:
            print "Error on the quantity format error test"
            test=False

    for i in stock:
        test2=i.add_trade("2017-08-10 00:00:00","m","bty",0.025)#expected not added - not buy or sell
        if test2==True:
            print "Error on the not buy or sell error test"
            test=False

    for i in stock:
        test2=i.add_trade("2017-08-10 00:00:00","m",10,0.025)#expected not added - not buy or sell
        if test2==True:
            print "Error on the not buy or sell error test"
            test=False

    for i in stock:
        test2=i.add_trade("2017-08-10 00:00:00",10,"buy","0.025")#expected not added - price format
        if test2==True:
            print "Error on the price format error test"
            test=False

    
    return test

