import sys
sys.path.append("..")
from stock import *
from getIndex import *

def testVolumeWeightedStockPrice(stock):
    for i in stock:
        print "The Volume Weighted Stock Price for "+i.getStockSymbole()+" is "+str(i.volumeWeightedStockPrice())
