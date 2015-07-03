"""
Created on 25.06.2015

@author: hohausjs
"""
import urllib2


class Crawl:

    to_crawl = []
    crawled = []

    def __init__(self):
        self.current_page = ''
        pass

    def get_next_href_from_html(self, htmlString):

        start_link = htmlString.find('<a href=')
        start_quote = htmlString.find('"', start_link)
        end_quote = htmlString.find('"', start_quote + 1)

        # check if an occurence has been found
        if start_link == -1 or start_quote == -1 or end_quote == -1:
            return "", -1

        print "start link"
        url = htmlString[start_quote + 1:end_quote]

        # check if url is empty
        if not url:
            return url, -1

        return url, end_quote

    def crawl_next_page_for_links(self):

        if not self.current_page:
            return []

        page = self.current_page
        links_list = []

        while page:
            new_url, end_quote = self.get_next_href_from_html(page)

            if end_quote != -1:
                links_list.append(new_url)
                page = page[end_quote:]
            else:
                page = None

        return links_list

    def load_next_page(self):

        self.current_page = ''

        try:
            page = urllib2.urlopen(self.to_crawl.pop()).read()
        except:
            page = None
            print 'Error loading page!'
            return -1

        try:
            page
        except:
            page = None
            print 'Error: page is empty!'
            return -1

        self.current_page = page

        return 1

    def add_url(self, url):
        # check if url is not already in the "toCrawl" list
        if url not in self.to_crawl:
            print "Adding url: [%s]" % url
            self.to_crawl.append(url)
