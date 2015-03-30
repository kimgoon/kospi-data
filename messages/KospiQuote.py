# Kospi Message for Quote Data

from KospiMessage import KospiMessage

class KospiQuote(KospiMessage):
  def __init__(self, data):
    KospiMessage.__init__(self, data)

    # define constants
    self.MSGNAME = "B6"

  def decode(self):
    if(self.data[0:2] != self.MSGNAME):
      return False
    self.ftype = self.data[0:2]
    self.info = self.data[2:4]
    self.shisang = self.data[4:5]
    self.xx_code = self.data[5:17]
    self.sequence = self.data[17:19]
    self.xx_code1 = self.data[19:21]
    self.bidaggr_size = self.data[21:27]
    self.bid1_sign = self.data[27:28]
    self.bid1_price = self.getFormattedPrice(self.data[28:33])
    self.bid1_size = self.data[33:39]
    self.bid2_sign = self.data[39:40]
    self.bid2_price = self.getFormattedPrice(self.data[40:45])
    self.bid2_size = self.data[45:51]
    self.bid3_sign = self.data[51:52]
    self.bid3_price = self.getFormattedPrice(self.data[52:57])
    self.bid3_size = self.data[57:63]
    self.bid4_sign = self.data[63:64]
    self.bid4_price =  self.getFormattedPrice(self.data[64:69])
    self.bid4_size = self.data[69:75]
    self.bid5_sign = self.data[75:76]
    self.bid5_price = self.getFormattedPrice(self.data[76:81])
    self.bid5_size = self.data[81:87]
    self.askaggr_size = self.data[87:93]
    self.ask1_sign = self.data[93:94]
    self.ask1_price = self.getFormattedPrice(self.data[94:99])
    self.ask1_size = self.data[99:105]
    self.ask2_sign = self.data[105:106]
    self.ask2_price = self.getFormattedPrice(self.data[106:111])
    self.ask2_size = self.data[111:117]
    self.ask3_sign = self.data[117:118]
    self.ask3_price = self.getFormattedPrice(self.data[118:123])
    self.ask3_size = self.data[123:129]
    self.ask4_sign = self.data[129:130]
    self.ask4_price = self.getFormattedPrice(self.data[130:135])
    self.ask4_size = self.data[135:141]
    self.ask5_sign = self.data[141:142]
    self.ask5_price = self.getFormattedPrice(self.data[142:147])
    self.ask5_size = self.data[148:153]
    self.bidvalid = self.data[153:158]
    self.bid1_order_num = self.data[158:162]
    self.bid2_order_num = self.data[162:166]
    self.bid3_order_num = self.data[166:170]
    self.bid4_order_num = self.data[170:174]
    self.bid5_order_num = self.data[174:178]
    self.askvalid = self.data[178:183]
    self.ask1_order_num =  self.data[183:187]
    self.ask2_order_num = self.data[187:191]
    self.ask3_order_num = self.data[191:195]
    self.ask4_order_num = self.data[195:199]
    self.ask5_order_num = self.data[199:203]
    self.current_time = self.data[203:211]
    self.xx_predictprice = self.getFormattedPrice(self.data[211:212])
    self.xx_predicttradeprice = self.getFormattedPrice(self.data[212:217])
    self.setDecoded(True)
    return True


  def getCSVString(self):
    if(self.getDecoded == False):
      return ""
    return ",".join((self.current_time,
                    self.xx_code,
                    self.sequence,
                    self.bid1_price,
                    self.bid1_size,
                    self.ask1_price,
                    self.ask1_size,
                    "",
                    ""))

  def parse_print(self):
    print "ftype: " + self.data[0:2]                 #2
    print "info: " + self.data[2:4]                  #4
    print "shisang_: " + self.data[4:5]              #5
    print "xxx_code: " + self.data[5:17]             #17
    print "xxx_seq: " + self.data[17:19]             #19
    print "xxx_code1: " + self.data[19:21]           #21
    print "agg bid size: " + self.data[21:27]        #27
    print "bid 1 sign: " + self.data[27:28]
    print "bid 1 price: " + self.data[28:33]
    print "bid 1 size: " + self.data[33:39]
    print "bid 2 sign: " + self.data[39:40]
    print "bid 2 price: " + self.data[40:45]
    print "bid 2 size: " + self.data[45:51]
    print "bid 3 sign: " + self.data[51:52]
    print "bid 3 price: " + self.data[52:57]
    print "bid 3 size: " + self.data[57:63]
    print "bid 4 sign: " + self.data[63:64]
    print "bid 4 price: " + self.data[64:69]
    print "bid 4 size: " + self.data[69:75]
    print "bid 5 sign: " + self.data[75:76]
    print "bid 5 price: " + self.data[76:81]
    print "bid 5 size: " + self.data[81:87]
    print "agg ask size: " + self.data[87:93]
    print "ask 1 sign: " + self.data[93:94]
    print "ask 1 price: " + self.data[94:99]
    print "ask 1 size: " + self.data[99:105]
    print "ask 2 sign: " + self.data[105:106]
    print "ask 2 price: " + self.data[106:111]
    print "ask 2 size: " + self.data[111:117]
    print "ask 3 sign: " + self.data[117:118]
    print "ask 3 price: " + self.data[118:123]
    print "ask 3 size: " + self.data[123:129]
    print "ask 4 sign: " + self.data[129:130]
    print "ask 4 price: " + self.data[130:135]
    print "ask 4 size: " + self.data[135:141]
    print "ask 5 sign: " + self.data[141:142]
    print "ask 5 price: " + self.data[142:147]
    print "ask 5 size: " + self.data[148:153]
    print "bid valid: " + self.data[153:158]
    #  print "bid 1 order_num: " + self.data[158:162]
    #  print "bid 2 order_num: " + self.data[162:166]
    #  print "bid 3 order_num: " + self.data[166:170]
    #  print "bid 4 order_num: " + self.data[170:174]
    #  print "bid 5 order_num: " + self.data[174:178]
    #  print "ask valid: " + self.data[178:183]
    #  print "ask 1 order_num: " + self.data[183:187]
    #  print "ask 2 order_num: " + self.data[187:191]
    #  print "ask 3 order_num: " + self.data[191:195]
    #  print "ask 4 order_num: " + self.data[195:199]
    #  print "ask 5 order_num: " + self.data[199:203]
    print "current time: " + self.data[203:211]
    print "predict price ?? " + self.data[211:212]
    print "predict trade price? " + self.data[212:217]
    eot = self.data[217:218]
    if(eot == "\xff"):
      print "OK"

  def print_raw(self):
    print self.data


