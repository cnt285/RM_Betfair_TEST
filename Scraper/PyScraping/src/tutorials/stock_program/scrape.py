'''
Created on 13 Nov 2014

Python Web Scraping Tutorial 5, 6, 7, 8 - Network Requests - https://www.youtube.com/watch?v=5FoSwMZ4uJg

Loading 1 minute data from bloomberg


@author: cnt285
'''

import urllib
import re
import json

symbolslist = open("all_symbols.txt").read()
symbolslist = symbolslist.split("\n")

for symbol in symbolslist:
    
    # create and write to he file
    myfile = open("daily_prices/" + symbol + ".txt", "w+") 
    myfile.close()
    
    htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+ symbol +":US")
    data = json.load(htmltext)
    datapoints = data['data_values']
    
    # append to file
    myfile = open("daily_prices/" + symbol + ".txt", "a")
    for point in datapoints:
        myfile.write(str(symbol) + "," + str(point[0]) + "," + str(point[1]) + "\n")
    myfile.close()
        
#         print "the number of points is ", len(datapoints)

# print datapoints[-1][1]
# print datapoints[len(datapoints)-1]