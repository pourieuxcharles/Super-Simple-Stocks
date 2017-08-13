import sys
from Test1d import *
from Test1PE import *
from Test1AddTrades import *
from Test1v import *
from Test1GBCE import *
sys.path.append("..")
from stock import *
   

   
stock=[]
stock.append(Stock("TEA","Common",0.00,"null",100))
stock.append(Stock("POP","Common",8.00,"null",100))
stock.append(Stock("ALE","Common",23.00,"null",60))
stock.append(Stock("GIN","Preferred",8.00,0.02,100))
stock.append(Stock("JOE","Common",13.00,"null",250))

allTest=True
#test dividended Yield
if testDividendYield(stock):
    print "Dividend Yield Ok"
else:
	allTest=False
	print "Error Dividend Yield"
	

#test PE ratio
if testPERatio(stock):
    print "PE Ratio Ok"
else:
	print "Error PE Ratio"
	allTest=False

#test add trade
if testAddTrades(stock):
    print "Add trades Ok"
else:
	print "Add trades error"
	allTest=False


#test volume Weighted Stock Price

if testVolumeWeightedStockPrice(stock):
    print "Volume Weigthed Stock Price Ok"
else:
	allTest=False
	print "Volume Weigthed Stock Price Error"





if testGBCE(stock):
	print "GBCE all share test Ok"
else:
	print "GBCE all share test Error"	
	allTest=False

if allTest:
	print "Tests completed: Ok"
else:
	print "Tests completed: Error"
