import urllib2


def getLinkFromIndex(htmlString):
    
    start_link = htmlString.find('<a href=')
    start_quote = htmlString.find('"', start_link)
    end_quote = htmlString.find('"', start_quote+1)
    
        # check if an occurence has been found
    if start_link == -1 or start_quote == -1 or end_quote == -1 :
        return "", -1
        
    print "start link"
    url = htmlString[start_quote+1:end_quote]
        
    return url, end_quote

def crawlPage(link):
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
    print page
    
    while page:
        new_url, end_quote = getLinkFromIndex(page)
        
        if end_quote != -1:
            print new_url
            page = page[end_quote:]
        else:
            page = False
    
    return 0
           
def getLinkToPage():
    return "http://ws-bb.de/"
    

def main():
    
#    start by asking for a link
    pageLink = getLinkToPage()
    print "got page " + pageLink
 
#   search this page for links
    links = crawlPage(pageLink)
    
    return 0


if __name__ == '__main__':
    main()

