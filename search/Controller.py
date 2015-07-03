__author__ = 'frosch'

from Crawl import Crawl


class Controller:
    def __init__(self):
        pass

    '''
    start a simple process
    by asking for an uri and search only this site / domain
    '''

    def start_simple(self):

        # get the crawler
        crawler = Crawl()

        crawler.add_url(self.ask_for_link())
        crawler.load_next_page()
        links = crawler.crawl_next_page_for_links()
        for link in links:
            crawler.add_url(link)

        pass

    '''
    this method asks for a link (console)
    '''
    def ask_for_link(self):
        # ragt nach einer url
        urlinput = raw_input("Bitte gib eine URL ein: \n")
        if urlinput.find('http://') == -1 or urlinput.find('https://') == -1:
            urlinput = "http://" + urlinput
        return urlinput
