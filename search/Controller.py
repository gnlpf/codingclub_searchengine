__author__ = 'frosch'

from Crawl import Crawl
from Index import Index

class Controller:
    def __init__(self):
        pass

    '''
    start a simple process
    by asking for an uri and search only this site / domain

    HINT:
    this can then be optimized like
    * scan all url's in a loop
    * be able to define how long to scan
        * like number of pages or time limit
    * define if the crawler should stay on one domain only
    '''
    def start_simple(self):

        # get the crawler
        crawler = Crawl()

        print "ask for an url to begin with..."
        origin = self.ask_for_link()

        print "begin crawling"
        crawler.add_url(origin)
        crawler.load_next_page()
        links = crawler.crawl_next_page_for_links()

        print "add collected links to link-list"
        for link in links:
            success, new_url = self.make_absolute_link(link, origin)
            if success:
                crawler.add_url(new_url)

        print "finished crawling, found following links on page: "
        # print all collected urls which still need to be crawled
        print crawler.get_all_urls()

        # continue with parsing contents
        # TODO
        keywords = crawler.extract_keywords()

        pass

    '''
    this method asks for a link (console)
    '''
    @staticmethod
    def ask_for_link():
        # ragt nach einer url
        urlinput = raw_input("Bitte gib eine URL ein: \n")
        if urlinput.find('http://') == -1 or urlinput.find('https://') == -1:
            urlinput = "http://" + urlinput
        return urlinput

    @staticmethod
    def make_absolute_link(link, origin):

        if len(link) < 4:
            return False, link

        # convert relative links, like "/kontakt.php"
        # to an absolute link: "http://..../kontakt.php"
        stringpart = link.split('://')
        new_url = ""

        # if link contains http or https then it is already an absolute link
        if len(stringpart) > 1:
            new_url = link

        else:
            # define required variables
            protocol = ''
            path = ''
            pathlen = 0
            domain = ''

            splitOrigin = origin.split('://')
            # check if link is ok, meaning there is a protocol part like "http://" or "https://"
            if len(splitOrigin) > 1:
                protocol = splitOrigin[0]
            else:
                # in error case, return -1
                return False, link

            # split for each /
            domainandpath = splitOrigin[1].split('/')
            domain = domainandpath[0]

            # path is everything after the domain

            new_url = protocol + '://' + domain

            if len(domainandpath) > 1:
                pathlen = len(domainandpath)
                for p in domainandpath[1:pathlen-1]:
                    path += p + "/"

            # link can have different forms
            # /mypage.html
            # ../mypage.html
            # mypage.html

            if link[0] == "/":
                new_url += link
            # elif link[0] == ".":
            #     new_url += path + link
            else:
                new_url += path + link

            print '-------'
            print 'origin: '
            print origin
            print 'protocol:'
            print protocol
            print 'domain'
            print domain
            print 'path'
            print path
            print 'new_url'
            print new_url
            print '--------'

        return True, new_url
