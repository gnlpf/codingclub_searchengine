"""
Created on 25.06.2015

@author: hohausjs
"""
# import urllib2
from Crawl import Crawl
from Controller import Controller


def getLinkToPage():
    """ fragt nach einer url """
    urlInput = raw_input("Bitte gib eine URL ein:")
    if urlInput.find('http://') == -1 or urlInput.find('https://') == -1:
        urlInput = "http://" + urlInput
    return urlInput


def makeAbsoluteLink(link, origin):
    # TODO
    # convert relative links, like "/kontakt.php"
    # to an absolute link: "http://..../kontakt.php"
    stringpart = link.split('://')

    # if link contains http or https then it is already an absolute link
    if len(stringpart) > 1:
        print link
        return link

    splitOrigin = origin.split('://')

    protocol = ''

    if len(splitOrigin) > 1:
        protocol = splitOrigin[0]

    domainAndPath = splitOrigin[1].split('/')
    domain = domainAndPath[0]

    print '-------'
    print 'origin: '
    print origin
    print 'protocol:'
    print protocol
    print 'domain'
    print domain
    print '--------'

    link = protocol + '://' + domain
    if len(path) > 1:
        link = link + '/' + path

    return link


def main():
    #    start by asking for a link
    toCrawl = []
    crawled = []
    toCrawl.append(getLinkToPage())
    crawlercl = Crawl()
    #    print "got page " + pageLink

    maxPagesSearched = 100
    i = 0

    #   search this page for links
    while len(toCrawl) > 0:
        # get first entry of "toCrawl" list
        crawl = toCrawl.pop()

        # TODO
        # ensure that this link is not contained in the "crawled" list        
        if crawl in crawled:
            # continue with the next loop
            continue

        links = crawlercl.crawl_next_page_for_links(crawl)

        # put into "crawled" list
        crawled.append(crawl)

        # add new found links to "toCrawl" list
        for link in links:
            # ensure that the link is not in the "crawled" list
            if link not in crawled:
                toCrawl.append(makeAbsoluteLink(link, crawl))
                print makeAbsoluteLink(link, crawl)

        # stop loop after .. iterations
        i += 1
        if i >= maxPagesSearched:
            break

    return 0


def run():

    # get an instance of the Controller
    Controller().start_simple()

    print "---------------------"
    print "programm has finished\n\nGood Bye"



if __name__ == '__main__':
    # main()
    run()