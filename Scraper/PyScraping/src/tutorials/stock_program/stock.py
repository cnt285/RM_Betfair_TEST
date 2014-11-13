'''
Created on 12 Nov 2014

Tutorial: Downloading Stock Data - https://www.youtube.com/watch?v=f2h41uEi0xU

Loading stock data from Yahoo Finance

@author: cnt285
'''

import urllib
import re

symbolfile = open("all_symbols.txt")

symbolslist = symbolfile.read()
newsymbolslist =  symbolslist.split("\n")

print newsymbolslist
print len(newsymbolslist)

# symbolslist = ["AAPL","SPY","GOOG","NFLX"]

i = 0
while i < len(newsymbolslist):
    url = "https://uk.finance.yahoo.com/q?s=" + newsymbolslist[i]  + "&ql=0"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()

    regex = '<span id="yfs_l84_' + str.lower(newsymbolslist[i]) + '">(.+?)</span>' 
    pattern = re.compile(regex)
    
    price = re.findall(pattern, htmltext)
    print "the price of ", newsymbolslist[i] , " is " , price
    
    i += 1