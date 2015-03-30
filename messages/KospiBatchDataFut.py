from KospiMessage import KospiMessage


# not tested

class KospiBatchDataFut(KospiMessage):
    def __init__(self, data):
        KospiMessage.__init__(self, data)
        self.data = data
        self.MSGNAME = "A0"

    def decode(self):
        if(self.data[0:2] != self.MSGNAME):
            return False

        self.DataType = self.data[0:2]
        self.InformationType = self.data[2:4]
        self.MarketType = self.data[4:5]
        self.IssueCount = self.data[5:10]
        self.TradingDate = self.data[10:18]
        self.IssueCode = self.data[18:30]
        self.IssueSeqNo = self.data[30:36]
        self.CommodityID = self.data[36:46]
        self.IssueCodeAbbr = self.data[46:55]
        self.IssueNameKor = self.data[55:135]
        self.IssueNameKorAbbr = self.data[135:175]
        self.IssueNameEng = self.data[175:255]
        self.IssueNameEngAbbr = self.data[255:295]

        # ...
        self.ExerciseType = self.data[354:355]
        self.NearbyMonth = self.data[397:398]
        self.ExpirationDate = self.data[398:406]
        self.Strike = self.getFormattedPrice(self.data[406:423])
        return True


    def getCSVString(self):
        if(self.getDecoded() == False):
            return ""
        return "stuff"


    def parse_print(self):
        print ",".join(self.DataType,
                       self.CommodityID,
                       self.IssueNameEng,
                       self.IssueNameEngAbbr,
                       self.NearbyMonth,
                       self.ExpirationDate,
                       self.Strike)
        pass

    def parse(self):
        pass



