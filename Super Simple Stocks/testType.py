import datetime

def isNumber(number):
    if (type(number)==int or type(number)==float) and number>0:
        return True
    else:
        return False


def testTimestamp(timestamp):
    try:
        timestamp=datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return timestamp
    except ValueError:
        print "Please check the format and if the date/time is accurate"
        return "Please check the format and if the date/time is accurate"
        

def testDatePast(timestamp):
    if timestamp>datetime.datetime.now():          
        return False
       
    else:
        return True

def sellOrBuy(word):
    if word.upper() not in {"SELL","BUY"}:       
        return False
       
    else:
        return True
