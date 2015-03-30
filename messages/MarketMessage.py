


class MarketMessage:
    def __init__(self, symbol):
        self.__symbol = symbol
        self.__msgType = "Q"
        self.__seqNum = 0
        self.__time = 0
        self.__bids = list()
        self.__bidSizes = list()
        self.__bidDepth = 0
        self.__asks = list()
        self.__askSizes = list()
        self.__askDepth = 0
        self.__trades = list()
        self.__tradeSizes = list()
        self.__tradeDepth = 0
        pass

    def test_01(self):
        self.__symbol = "SPY"
        self.__seqNum = 0
        self.__msgType = "Q"
        self.__time = 103023234
        self.__bids.append((600, 164.80))
        self.__bids.append((1600, 164.60))
        self.__bids.append((2600, 164.50))
        self.__bidDepth = len(self.__bids)

        self.__asks.append((200, 164.90))
        self.__asks.append((600, 165.00))
        self.__askDepth = len(self.__asks)

        self.__trades.append((100, 164.90))
        self.__tradeDepth = len(self.__trades)

    # define properties
    def get_symbol(self):
        return self.__symbol

    def symbol(self, symbol):
        self.__symbol = symbol

    def getMsgType(self):
        return self.__msgType

    def msgType(self, msgType):
        self.__msgType = msgType

    def getSeqNum(self):
        return self.__seqNum

    def seqNum(self, seqNum):
        self.__seqNum = seqNum

    def getTime(self):
        return self.__time

    def time(self, time):
        self.__time = time

    def getBidDepth(self):
        return self.__bidDepth

    def getAskDepth(self):
        return self.__askDepth

    def getTradeDepth(self):
        return self.__tradeDepth

    def getBid(self, idx):
        if(idx < self.__bidDepth):
            return (self.__bids[idx][0], self.__bids[idx][1])

    def getAsk(self, idx):
        if(idx < self.__askDepth):
            return (self.__asks[idx][0], self.__asks[idx][1])

    def getTrade(self, idx):
        if(idx < self.__tradeDepth):
            return (self.__trades[idx][0], self.__trades[idx][1])

    def rplBid(self, idx, size, price):
        if(idx < self.__bidDepth):
            self.__bids[idx] = (size, price)
            return True
        else:
            return False

    def rplAsk(self, idx, size, price):
        if(idx < self.__askDepth):
            self.__asks[idx] = (size, price)
            return True
        else:
            return False

    def rplTrade(self, idx, size, price):
        if(idx < self.__tradeDepth):
            self.__trades[idx] = (size, price)
            return True
        else:
            return False

    def addBid(self, size, price):
        self.__bids.append((size, price))
        self.__bidDepth = len(self.__bids)

    def addAsk(self, size, price):
        self.__asks.append((size, price))
        self.__askDepth = len(self.__asks)

    def addTrade(self, size, price):
        self.__trades.append((size, price))
        self.__tradeDepth = len(self.__trades)


    def clearAll(self):
        del self.__bids[0:]
        self.__bidDepth = 0

        del self.__asks[0:]
        self.__askDepth = 0

        del self.__trades[0:]
        self.__tradeDepth = 0


    def pretty(self):
        print "%-10d %10s %12d %10s" % (self.__seqNum, self.__symbol, self.__time, self.__msgType)
        maxDepth = max(self.getBidDepth(), self.getAskDepth(), self.getTradeDepth())
        for i in xrange(maxDepth):
            bidstr = ""
            if(i < self.getBidDepth()):
                bidstr = "%5d@%.5f" % (self.__bids[i][0], self.__bids[i][1])

            askstr = ""
            if(i < self.getAskDepth()):
                askstr = "%5d@%.5f" % (self.__asks[i][0], self.__asks[i][1])

            tradestr = ""
            if(i < self.getTradeDepth()):
                tradestr = "%5d@%.5f" % (self.__trades[i][0], self.__trades[i][1])

            print "%-2d %20s %20s %20s" % (i, bidstr, askstr, tradestr)
        print ""

if __name__ == "__main__":
    msg = MarketMessage("")
    msg.test_01()
    msg.pretty()

    msg.seqNum(1)
    msg.addAsk(2500, 165.5)
    msg.pretty()

    msg.seqNum(2)
    msg.addBid(2600, 164.1)
    msg.addTrade(200, 164.95)
    msg.pretty()

    msg.seqNum(3)
    msg.clearAll()
    msg.pretty()

    msg.seqNum(4)
    msg.addBid(2600, 164.1)
    msg.addTrade(200, 164.95)
    msg.pretty()

