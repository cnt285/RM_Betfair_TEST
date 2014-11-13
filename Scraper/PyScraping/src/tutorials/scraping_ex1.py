'''
Created on 12 Nov 2014

Follows list of tutorial videos from: https://www.youtube.com/watch?v=kPhZDsJUXic

@author: cnt285
'''

import urllib
import re

urls = ["http://google.com", "http://nytimes.com", "http://cnn.com", "http://facebook.com"]
i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)


while i < len(urls):
    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    
    titles = re.findall(pattern, htmltext)
    
    print titles
    
    i += 1

# if __name__ == '__main__':
#     pass