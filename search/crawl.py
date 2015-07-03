'''
Created on 25.06.2015

@author: hohausjs
'''
import urllib2

class Crawl:

    def getLinkFromIndex(self, htmlString):

        start_link = htmlString.find('<a href=')
        start_quote = htmlString.find('"', start_link)
        end_quote = htmlString.find('"', start_quote+1)

        # check if an occurence has been found
        if start_link == -1 or start_quote == -1 or end_quote == -1 :
            return "", -1

        print "start link"
        url = htmlString[start_quote+1:end_quote]

        # check if url is empty
        if not url:
            return url, -1

        return url, end_quote

    def crawlPage(self, link):
        
        try:
            page = urllib2.urlopen(link).read()
            
        except urllib2.HTTPError, e:
            print 'A problem occured while loading the page [' + link + ']. Please try again. ' + e
            
            return
        
        try:
            page
        except:
            page = "empty"
            return
    #    print page
        linksList = []
        
        while page:
            new_url, end_quote = self.getLinkFromIndex(page)
            
            if end_quote != -1:
                linksList.append(new_url)
                page = page[end_quote:]
            else:
                page = None
        
        return linksList