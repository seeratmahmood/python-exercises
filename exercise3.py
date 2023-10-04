import random
from time import time

def getPriceList(length):
  priceList = list()
  for i in range(length):
    priceList.append(random.randrange(1,100))
  return priceList

print(getPriceList(100))


def getMin(sharePrices):
  min = None
  for price in sharePrices:
    if min is None:
      min = price
    elif price < min:
      min = price
  return min

def getMax(sharePrices):
  max = None
  for price in sharePrices:
    if max is None:
      max = price
    elif price > max:
      max = price
  return max
  
def getAverage(sharePrices):
  sum = 0
  for price in sharePrices:
    sum += price
  return sum / len(sharePrices) 
  
 
class Stock:
  def __init__(self, name):
    self.name = name
    self.buyOrders = list()
    self.sellOrders = list()
    
class Exchange:
  def __init__(self):
    self.stockList = list([Stock('APPL'),
                          Stock('MSFT'),
                          Stock('GOOG'),
                          Stock('AMZN'),
                          Stock('TSLA'),
                          Stock('FB'),
                          Stock('TSM'),
                          Stock('NVDA'),
                          Stock('V'),
                          Stock('JNJ'),
                          Stock('UNH'),
                          Stock('JPM'),
                          Stock('BAC'),
                          Stock('WMT'),
                          Stock('PG'),
                          Stock('HD'),
                          Stock('MA'),
                          Stock('BABA'),
                          Stock('XOM'),
                          Stock('PFE'),
                          Stock('ASML'),
                          Stock('TM'),
                          Stock('NTES'),
                          Stock('DIS'),
                          Stock('KO'),
                          Stock('CSCO'),
                          Stock('CVX'),
                          Stock('ABDE'),
                          Stock('PEP'),
                          Stock('ABBV')])

  def getStockMin(self, stock):
    buyPrices = [order[1] for order in stock.buyOrders]
    sellPrices = [order[1] for order in stock.sellOrders]
    buyMin = getMin(buyPrices)
    sellMin = getMin(sellPrices)
    if buyMin <= sellMin:
      stockMin = buyMin
    else:
       stockMin = sellMin
    return stockMin

  def getStockMax(self, stock):
    buyPrices = [order[1] for order in stock.buyOrders]
    sellPrices = [order[1] for order in stock.sellOrders]
    buyMax = getMax(buyPrices)
    sellMax = getMax(sellPrices)
    if buyMax >= sellMax:
      stockMax = buyMax
    else:
       stockMax = sellMax
    return stockMax

  def getStockAverage(self, stock):
    buyPrices = [order[1] for order in stock.buyOrders]
    sellPrices = [order[1] for order in stock.sellOrders]
    buyAverage = getAverage(buyPrices)
    sellAverage = getAverage(sellPrices)
    return (buyAverage + sellAverage) / 2

  def addOrder(self, orderType, name, quantity, price):
    for stock in self.stockList: #search for specified stock
      if stock.name == name:
        quantity = self.matchOrder(stock, orderType, quantity, price) #attempt to match order
        if quantity > 0: #if order is not fully completed, store order information
          print('New ' + name + ' order: ' + orderType + ' ' + str(quantity) + ' at ' + str(price))
          if orderType == 'buy':
            stock.buyOrders.append([quantity, price, time()])
          elif orderType == 'sell':
            stock.sellOrders.append([quantity, price, time()])

  def matchOrder(self, stock, orderType, quantity, price):
    #attempts to match new order to existing orders, returns the remaining quantity of the new order
    if orderType == 'buy': #if buy order find matching sell order
      searchList = stock.sellOrders
    elif orderType == 'sell': #if sell order find matching buy order
      searchList = stock.buyOrders
    index = 0
    while index < len(searchList): # search potential matches
      if searchList[index][1] == price: 
        if searchList[index][0] == quantity:
          print(str(searchList[index][0]) + ' ' + stock.name + ' shares bought at ' + str(price) + ' per share')
          quantity = 0
          searchList.pop(index)
          return quantity
        elif searchList[index][0] >= quantity:
          print(str(quantity) + ' ' + stock.name + ' shares bought at ' + str(price) + ' per share')
          searchList[index][0] -= quantity
          quantity = 0
          return quantity 
        elif searchList[index][0] <= quantity:
          print(str(searchList[index][0]) + ' ' + stock.name + ' shares bought at ' + str(price) + ' per share')
          quantity -= searchList[index][0]
          searchList.pop(index)
          continue
      index += 1
    return quantity

  def closestOrders(self):
    closestPair = list([None, None])
    for stock in self.stockList:
      for order in stock.buyOrders:
        closest = findClosest(order)
        if closestPair[0] == None:
          closestPair = [order, closest]
        else:
          if abs(closestPair[0][2] - closestPair[1][2]) > abs(order[2] - closest[2]):
            closestPair = [order, closest]
      for order in stock.sellOrders:
        closest = findClosest(order)
        if closestPair[0] == None:
            closestPair = [order, closest]
        else:
          if abs(closestPair[0][2] - closestPair[1][2]) > abs(order[2] - closest[2]):
            closestPair = [order, closest]
    print('The time Between closest orders is: ' + str(abs(closestPair[0][2] - closestPair[1][2])))

  def findClosest(self, order):
    closest = None
    for stock in self.stockList:
      for order2 in stock.buyOrders:
        if closest == None:
          closest = order2
        else:
          if abs(order[2] - closest[2]) > abs(order[2] - order2[2]):
            closest = order2
      for order2 in stock.sellOrders:
        if closest == None:
          closest = order2
        else:
          if abs(order[2] - closest[2]) > abs(order[2] - order2[2]):
            closest = order2
    return closest

stocks = list(['APPL','MSFT','GOOG','AMZN','TSLA','FB','TSM','NVDA','V','JNJ','UNH','JPM','BAC','WMT','PG','HD','MA','BABA','XOM','PFE','ASML','TM','NTES','DIS','KO','CSCO','CVX','ABDE','PEP','ABBV'])

exchange = Exchange()
for i in range(50):
  exchange.addOrder('buy', stocks[random.randrange(0,len(stocks))], random.randrange(1,10), random.randrange(10,30))
for i in range(50):
  exchange.addOrder('sell', stocks[random.randrange(0,len(stocks))], random.randrange(1,10), random.randrange(10,30))
     