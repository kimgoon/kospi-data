#!/usr/bin/python

# purpose: parses out the quote and trade messages from the kospi
#          market data file

import sys
import argparse

sys.path.append('messages')

import KospiMessage
import KospiQuote
import KospiTrade
import KospiTradeQuote
import MarketMessage


# define some helper functions
def writeToFileOrConsole(handle, line):
    if(handle == None):
        print line
    else:
        handle.write(line+"\n")

def handleKospiQuote(quote):
    mktMsg = MarketMessage.MarketMessage("")
    mktMsg.symbol(quote.xx_code)
    mktMsg.msgType("QT")
    msgType = mktMsg.getMsgType()
    mktMsg.seqNum(int(quote.sequence))
    mktMsg.time(int(quote.current_time))
    if(int(quote.bid1_size) > 0):
        mktMsg.addBid(int(quote.bid1_size), float(quote.bid1_price))
    if(int(quote.bid2_size) > 0):
        mktMsg.addBid(int(quote.bid2_size), float(quote.bid2_price))
    if(int(quote.bid3_size) > 0):
        mktMsg.addBid(int(quote.bid3_size), float(quote.bid3_price))
    if(int(quote.bid4_size) > 0):
        mktMsg.addBid(int(quote.bid4_size), float(quote.bid4_price))
    if(int(quote.bid5_size) > 0):
        mktMsg.addBid(int(quote.bid5_size), float(quote.bid5_price))
    if(int(quote.ask1_size) > 0):
        mktMsg.addAsk(int(quote.ask1_size), float(quote.ask1_price))
    if(int(quote.ask2_size) > 0):
        mktMsg.addAsk(int(quote.ask2_size), float(quote.ask2_price))
    if(int(quote.ask3_size) > 0):
        mktMsg.addAsk(int(quote.ask3_size), float(quote.ask3_price))
    if(int(quote.ask4_size) > 0):
        mktMsg.addAsk(int(quote.ask4_size), float(quote.ask4_price))
    if(int(quote.ask5_size) > 0):
        mktMsg.addAsk(int(quote.ask5_size), float(quote.ask5_price))
    mktMsg.pretty()


def handleKospiTradeQuote(quote):
    mktMsg = MarketMessage.MarketMessage("")
    mktMsg.symbol(quote.xx_code)
    mktMsg.msgType("TRQT")
    mktMsg.seqNum(int(quote.sequence))
    mktMsg.time(int(quote.trade_time))
    if(int(quote.bid1_size) > 0):
        mktMsg.addBid(int(quote.bid1_size), float(quote.bid1_price))
    if(int(quote.bid2_size) > 0):
        mktMsg.addBid(int(quote.bid2_size), float(quote.bid2_price))
    if(int(quote.bid3_size) > 0):
        mktMsg.addBid(int(quote.bid3_size), float(quote.bid3_price))
    if(int(quote.bid4_size) > 0):
        mktMsg.addBid(int(quote.bid4_size), float(quote.bid4_price))
    if(int(quote.bid5_size) > 0):
        mktMsg.addBid(int(quote.bid5_size), float(quote.bid5_price))
    if(int(quote.ask1_size) > 0):
        mktMsg.addAsk(int(quote.ask1_size), float(quote.ask1_price))
    if(int(quote.ask2_size) > 0):
        mktMsg.addAsk(int(quote.ask2_size), float(quote.ask2_price))
    if(int(quote.ask3_size) > 0):
        mktMsg.addAsk(int(quote.ask3_size), float(quote.ask3_price))
    if(int(quote.ask4_size) > 0):
        mktMsg.addAsk(int(quote.ask4_size), float(quote.ask4_price))
    if(int(quote.ask5_size) > 0):
        mktMsg.addAsk(int(quote.ask5_size), float(quote.ask5_price))
    if(int(quote.trade_size) > 0):
        mktMsg.addTrade(int(quote.trade_size), float(quote.trade_price))
    mktMsg.pretty()

def handleKospiTrade(quote):
    mktMsg = MarketMessage.MarketMessage("")
    mktMsg.symbol(quote.xx_code)
    mktMsg.msgType("TR")
    mktMsg.seqNum(int(quote.sequence))
    mktMsg.time(int(quote.trade_time))
    if(int(quote.trade_size) > 0):
        mktMsg.addTrade(int(quote.trade_size), float(quote.trade_price))

    mktMsg.pretty()

# define some globals

sys.stderr.write("script started...\n")

# TODO parse out command lines to get options
parser = argparse.ArgumentParser(description="Parse out the Kospi data file")
parser.add_argument('-f', '--inputfile', help='file for input')
parser.add_argument('-o', '--outputfile', help='file for output')
parser.add_argument('-m', '--msgtype', help='type of msg (default=all, 0=quote and trade,\
                                             1=quote, 2=trade, 3=tradequote)')

print_quote = True
print_trade = True
print_tradequote = True
file_name = "~/Downloads/Kospi_Data_2013_07_11.txt"

cmd_results = parser.parse_args()

if(cmd_results.msgtype == "0"):
    print_tradequote = False
elif(cmd_results.msgtype == "1"):
    print_trade = False
    print_tradequote = False
elif(cmd_results.msgtype == "2"):
    print_quote = False
    print_tradequote = False
elif(cmd_results.msgtype == "3"):
    print_quote = False
    print_trade = False
elif(cmd_results.msgtype == "4"):
    print_quote = False
    print_trade = False
    print_tradequote = False

outputfile = None
output_handle = None

print_quote = True
print_trade = True
print_tradequote = True

if(cmd_results.outputfile != None):
    outputfile = cmd_results.outputfile
    output_handle = open(outputfile, 'w')
    print "INFO writing output to file="+outputfile

if(cmd_results.inputfile != None):
    file_name = cmd_results.inputfile


sys.stderr.write("opening file:" + file_name + "\n")

file_handle = open(file_name)

writeToFileOrConsole(output_handle, KospiQuote.KospiQuote.getCSVHeader())

for line in file_handle.readlines():
    isKospi200 = KospiMessage.KospiMessage.isSecTypeKospi200(line)
    msgtype = KospiMessage.KospiMessage.getMessageType(line)

    if(isKospi200 == True):

        if(msgtype == "QUOTE" and print_quote):
            kq = KospiQuote.KospiQuote(line)
            if(kq.decode() == True):
#               print kq.getCSVString()
                #writeToFileOrConsole(output_handle, kq.getCSVString())
                handleKospiQuote(kq)
            else:
                print "ERROR failed to decode KospiQuote"

        elif(msgtype == "TRADE" and print_trade):
            kt = KospiTrade.KospiTrade(line)
            if(kt.decode() == True):
                handleKospiTrade(kt)
#                writeToFileOrConsole(output_handle, kt.getCSVString())
#        print kt.getCSVString()
            else:
                print "ERROR failed to decode KospiTrade"
        elif(msgtype == "TRADEQUOTE" and print_tradequote):
            ktq = KospiTradeQuote.KospiTradeQuote(line)
            if(ktq.decode() == True):
                handleKospiTradeQuote(ktq)
#                writeToFileOrConsole(output_handle, ktq.getCSVString())
#        print ktq.getCSVString()
            else:
                print "ERROR failed to decode KospiTradeQuote"
        elif(msgtype == "BATCHDATA"):
            bd = KospiBatchDataFut.KospiBatchDataFut(line)
            if(bd.decode() == True):
                bd.parse_print()
            else:
                print "Failed to decode BatchData"

if(output_handle != None):
    output_handle.close()

sys.stderr.write("script exited\n")


