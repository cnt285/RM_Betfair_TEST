'''
Created on 13 Nov 2014

Multithreaded Python Tutorial 9 - https://www.youtube.com/watch?v=CXQ3QoT5bdQ

Introduce using python threads to load data faster

@author: cnt285
'''

from threading import Thread
import urllib
import re

def th(ur):
    base_url = "https://uk.finance.yahoo.com/q/bc?s=" + ur
#     regex = "<title>.+?</title>"
    regex = '<span id="yfs_l84_' + str.lower(ur) + '">(.+?)</span>' 
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(base_url).read()
    results = re.findall(pattern, htmltext)
    print "the price of " + str(ur) + " is " + str(results)
    
# urls = "http://google.com http://cnn.com http://yahoo.com http://wikipedia.com".split()

symbolslist = open("all_symbols.txt").read()
symbolslist = symbolslist.split("\n")
print symbolslist

threadlist = []

for u in symbolslist:
    t = Thread(target = th, args=(u,))
    t.start()
    threadlist.append(t)
    
for b in threadlist:
    b.join()
    
