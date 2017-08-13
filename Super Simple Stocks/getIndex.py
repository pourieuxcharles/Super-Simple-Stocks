from stock import *

def getIndex(stockSymbole,stock):
	for i in stock:
		if i.getStockSymbole()==stockSymbole:
			return stock.index(i)
