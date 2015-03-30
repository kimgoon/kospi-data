# Kospi Message for TradeAndQuote Data

from KospiMessage import KospiMessage

class KospiTradeQuote(KospiMessage):
  def __init__(self, data):
    KospiMessage.__init__(self, data)
    self.data = data
    self.MSGNAME = "G7"


  def decode(self):
    if(self.data[0:2] != self.MSGNAME):
      return False
    self.ftype = self.data[0:2]
    self.info = self.data[2:4]
    self.shisang = self.data[4:5]
    self.xx_code = self.data[5:17]
    self.sequence = self.data[17:19]
    self.trade_sign = self.data[19:20]
    self.trade_price = self.getFormattedPrice(self.data[20:25])
    self.trade_size = self.data[25:31]
    self.trade_status = self.data[31:33]
    self.trade_time = self.data[33:41]

    # ????
    self.recent_contractprice = self.getFormattedPrice(self.data[41:46])
    self.contractprice = self.getFormattedPrice(self.data[46:51])
    self.openprice_sign = self.data[51:52]
    self.openprice_price = self.getFormattedPrice(self.data[52:57])
    self.highprice_sign = self.data[57:58]
    self.highprice_price = self.getFormattedPrice(self.data[58:63])
    self.midprice_sign = self.data[63:64]
    self.midprice_price = self.getFormattedPrice(self.data[64:69])
    self.prevprice_sign = self.data[69:70]
    self.prevprice_price = self.getFormattedPrice(self.data[70:75])
    self.noojuk_trade_size = self.data[75:82]
    self.noojuk_guhraedaegum = self.data[82:94]

    self.status_code = self.data[94:96]

    self.bidaggr_size = self.data[96:102]
    self.bid1_sign = self.data[102:103]
    self.bid1_price = self.getFormattedPrice(self.data[103:108])
    self.bid1_size = self.data[108:114]
    self.bid2_sign = self.data[114:115]
    self.bid2_price = self.getFormattedPrice(self.data[115:120])
    self.bid2_size = self.data[120:126]
    self.bid3_sign = self.data[126:127]
    self.bid3_price = self.getFormattedPrice(self.data[127:132])
    self.bid3_size = self.data[132:138]
    self.bid4_sign = self.data[138:139]
    self.bid4_price =  self.getFormattedPrice(self.data[139:144])
    self.bid4_size = self.data[144:150]
    self.bid5_sign = self.data[150:151]
    self.bid5_price = self.getFormattedPrice(self.data[151:156])
    self.bid5_size = self.data[156:162]
    self.askaggr_size = self.data[162:168]
    self.ask1_sign = self.data[168:169]
    self.ask1_price = self.getFormattedPrice(self.data[169:174])
    self.ask1_size = self.data[174:180]
    self.ask2_sign = self.data[180:181]
    self.ask2_price = self.getFormattedPrice(self.data[181:186])
    self.ask2_size = self.data[186:192]

    self.ask3_sign = self.data[192:193]
    self.ask3_price = self.getFormattedPrice(self.data[193:198])
    self.ask3_size = self.data[198:204]
    self.ask4_sign = self.data[204:205]
    self.ask4_price = self.getFormattedPrice(self.data[205:210])
    self.ask4_size = self.data[210:216]
    self.ask5_sign = self.data[216:217]
    self.ask5_price = self.getFormattedPrice(self.data[217:222])
    self.ask5_size = self.data[222:228]

    i = 228
    self.bidaggr_order_num = self.data[i:i+5]
    i+=5
    self.bid1_order_num = self.data[i:i+4]
    i+=4
    self.bid2_order_num = self.data[i:i+4]
    i+=4
    self.bid3_order_num = self.data[i:i+4]
    i+=4
    self.bid4_order_num = self.data[i:i+4]
    i+=4
    self.bid5_order_num = self.data[i:i+4]
    i+=4

    self.askaggr_order_num = self.data[i:i+5]
    i+=5
    self.ask1_order_num = self.data[i:i+4]
    i+=4
    self.ask2_order_num = self.data[i:i+4]
    i+=4
    self.ask3_order_num = self.data[i:i+4]
    i+=4
    self.ask4_order_num = self.data[i:i+4]
    i+=4
    self.ask5_order_num = self.data[i:i+4]
    self.setDecoded(True)
    return True


  def getCSVString(self):
      if(self.getDecoded() == False):
        return ""
      return ",".join((self.trade_time,
                       self.xx_code,
                       self.sequence,
                       self.bid1_price,
                       self.bid1_size,
                       self.ask1_price,
                       self.ask1_size,
                       self.trade_price,
                       self.trade_size))


  def parse_print(self):
    pass


  def parse(self):
    pass
