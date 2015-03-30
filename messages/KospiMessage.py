# base class for all Kospi Message types, defines a few common methods
# for use by all classes
class KospiMessage:
    def __init__(self, data):
        self.data = data
        self.isDecoded = False

    def getFormattedPrice(self, data):
        if(len(data) == 5):
            return data[0:3] + "." + data[3:5]
        else:
            return "xxx.yy"

    def getDecoded(self):
        return self.isDecoded

    def setDecoded(self, flag):
        self.isDecoded = flag

    @staticmethod
    def isSecTypeKospi200(data):
        if(len(data) < 4):
            return False

        if(data[2:4] == "01"):
            return True

        return False

    @staticmethod
    def getMessageType(data):
        if(len(data) < 2):
            return ""

        msgtype = data[0:2]
        if(msgtype == "B6"):
            return "QUOTE"
        elif(msgtype == "A3"):
            return "TRADE"
        elif(msgtype == "G7"):
            return "TRADEQUOTE"
        elif(msgtype == "A6"):
            return "SETTLE"
        elif(msgtype == "A7"):
            return "JANG_OON_YOUNG"
        elif(msgtype == "A0"):
            return "BATCHDATA"
        return ""

    @staticmethod
    def getCSVHeader():
        return "TIME,PRODUCT,SEQUENCE,BID1_PX,BID1_SZ,ASK1_PX,ASK1_SZ,TRADE_PX,TRADE_SZ"
