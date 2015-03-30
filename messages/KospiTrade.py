# Kospi Message for Trade data
from KospiMessage import KospiMessage

class KospiTrade(KospiMessage):
  def __init__(self, data):
    KospiMessage.__init__(self, data)
    # define constants
    self.MSGNAME = "A3"

  def decode(self):
    if(self.data[0:2] != self.MSGNAME):
      return False
    self.ftype = self.data[0:2]
    self.sectype = self.data[2:4]
    self.shijang = self.data[4:5]
    self.xx_code = self.data[5:17]
    self.sequence =  self.data[17:19]
    self.trade_sign = self.data[19:20]
    self.trade_price = self.getFormattedPrice(self.data[20:25])
    self.trade_size =  self.data[25:31]
    self.trade_code = self.data[31:33]
    self.trade_time = self.data[33:41]
    self.setDecoded(True)
    return True


  def printdata(self):
    if(self.getDecoded() == False):
      return
    print "ftype: " + self.ftype
    print "info: " + self.sectype
    print "shisang_: " + self.shijang
    print "xxx_code: " + self.xx_code
    print "xxx_seq: " + self.sequence
    print "trade sign: " + self.trade_sign
    print "trade price: " + self.trade_price
    print "trade size: " + self.trade_size
    print "trade code: " + self.trade_code
    print "trade time: " + self.trade_time


  def getCSVString(self):
    if(self.getDecoded() == False):
      return ""
    return ",".join((self.trade_time,
                     self.xx_code,
                     self.sequence,
                     "",
                     "",
                     "",
                     "",
                     self.trade_price,
                     self.trade_size))






