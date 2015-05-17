# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 07:31:36 2015

@author: frosch
"""

import urllib2
import numpy as np
from bs4 import BeautifulSoup
#soup = BeautifulSoup(urllib2.urlopen("http://www.armax.de").read())
#soup = BeautifulSoup("<html>data</html>")

def findImages(string):
    soup = BeautifulSoup(string)
    print soup.body.img['src']

    start_link = string.find('<img')
    start_src = string.find('src=', start_link)
    start_quote = string.find('"', start_src)
    end_quote = string.find('"', start_quote+1)
    
    if start_link == -1 or start_quote == -1 or end_quote == -1 :
        return "", -1
    url = string[start_quote+1:end_quote]
    
    if not url:
        print "No files found"
        return False
    return url, end_quote
    
    
    
def getLinkFromIndex(htmlString):
    
    start_link = htmlString.find('<a href=')
    start_quote = htmlString.find('"', start_link)
    end_quote = htmlString.find('"', start_quote+1)
    
    # check if an occurence has been found
    if start_link == -1 or start_quote == -1 or end_quote == -1 :
        return "", -1
        
    url = htmlString[start_quote+1:end_quote]
    
    # check if url is empty
    if not url:
        return url, -1
        
    return url, end_quote
    


def crawlPage(link):
    
    try:
        page = urllib2.urlopen(link).read()
        string = urllib2.urlopen(link).read()
    except urllib2.HTTPError, e:
        print 'A problem occured while loading the page [' + link + ']. Please try again. ' + e
        return
    except ValueError, e:
        print 'false url: ' 
        print e.message
        return
        
    bildlist = []
    
    while page:
        new_url, end_quote = findImages(page)
        
        if new_url:
            bildlist.append(new_url)
            page = page[end_quote:]
        else:
            page = None
    
    return bildlist
    



def getLinkToPage():
    
    return raw_input("Bitte Link eigeben")



def main():
    
#    start by asking for a link
    pageLink = getLinkToPage()
    print "got page " + pageLink
 
 #   search this page for links
    bildlist = crawlPage(pageLink)
    print bildlist
    return 0


if __name__ == '__main__':
	main()

