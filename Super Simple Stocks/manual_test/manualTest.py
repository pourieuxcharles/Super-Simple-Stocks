import sys
from mDividendYield import *
from mPERatio import *
from mAddTrade import *
from mVolumeWeightedSotckPrice import *
sys.path.append("..")
from trade import *
from stock import *
from getIndex import *
from GBCE import *


import datetime
import math
   

   
stock=[]
stock.append(Stock("TEA","Common",0.00,"null",100))
stock.append(Stock("POP","Common",8.00,"null",100))
stock.append(Stock("ALE","Common",23.00,"null",60))
stock.append(Stock("GIN","Preferred",8.00,0.02,100))
stock.append(Stock("JOE","Common",13.00,"null",250))

#test Dividend Yield
#testDividendYield(stock)

#test P/E ratio
#testPE_ratio(stock)

#test add trade
testAddTrade(stock)

#test Volume Weighted Stock Price based on trades in past 15 minutes
testVolumeWeightedStockPrice(stock)

#test GBCE
print "The GBCE all index share is "+ str(GBCE(stock))

