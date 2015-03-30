# Kospi Message for Option Quote Data

from KospiMessage import KospiMessage

class KospiOptionQuote(KospiMessage):
    def __init__(self, data):
        KospiMessage.__init__(self, data)

        # define constants
        self.MSGNAME = "B6"


    def decode(self):
        pass

    def getCSVString(self):
        pass


    def parse_print(self):
        pass
