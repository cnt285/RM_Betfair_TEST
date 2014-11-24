'''
Created on 13 Nov 2014

Multithreaded Python Tutorial 9 - https://www.youtube.com/watch?v=CXQ3QoT5bdQ
Tutorial 10 - Python MySQL Database

- Install mysqlserver: sudo apt-get install mysql-server
- Install python mysql: sudo apt-get install python-mysqldb



Introduce using python threads to load data faster

@author: cnt285
'''

from threading import Thread
import urllib
import re
import MySQLdb

gmap = {}


def th(ur):
    base_url = "https://uk.finance.yahoo.com/q/bc?s=" + ur
#     regex = "<title>.+?</title>"
    regex = '<span id="yfs_l84_' + str.lower(ur) + '">(.+?)</span>' 
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(base_url).read()
    results = re.findall(pattern, htmltext)
    
    try:
        gmap[ur] = results[0]
    except:
        print "got an error"
    
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
    





host_name = "localhost"
user_name = "root"
password = ""

conn = MySQLdb.connect(host=host_name, user=user_name, passwd=password, db="stock_data")

query = "INSERT INTO tutorial (symbol) values ('AAPL')"
x = conn.cursor()
x.execute(query)
row = x.fetchall()