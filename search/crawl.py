'''
Created on 25.06.2015

@author: hohausjs
'''
import urllib2



class Crawl:

    
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
    
