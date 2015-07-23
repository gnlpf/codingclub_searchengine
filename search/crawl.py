"""
Created on 25.06.2015

@author: hohausjs
@author: froeser
"""
import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup as bs

class Crawl:

    to_crawl = []
    crawled = []

    def __init__(self):
        self.current_page = ''
        self.current_link = ''
        pass

    def get_next_href_from_html(self, htmlString):

        start_link = htmlString.find('<a href=')
        start_quote = htmlString.find('"', start_link)
        end_quote = htmlString.find('"', start_quote + 1)

        # check if an occurence has been found
        if start_link == -1 or start_quote == -1 or end_quote == -1:
            return "", -1

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
                links_list.append(self.convert_to_absolute_link(new_url))
                page = page[end_quote:]
            else:
                page = None

        return links_list

    def convert_to_absolute_link(self, link):
        parsed = urlparse.urlparse(link)

        # check protocol and domain
        if parsed[0] and parsed[1]:
            # then absolute link, simply return
            return link

        if not parsed[2]:
            return ''
        else:
            parsed_original_link = urlparse.urlparse(self.current_link)

            if parsed_original_link[0] and parsed_original_link[1]:
                link = parsed_original_link[0] + "://" + parsed_original_link[1]

            # check if path starts with "/"
            path = parsed[2]
            if path[0] != "/":
                link += "/"

            link += path

        return link

    def load_next_page(self):

        self.current_page = ''
        self.current_link = self.to_crawl.pop()

        try:
            page = urllib2.urlopen(self.current_link).read()
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

    def get_all_urls(self):
        return self.to_crawl

    def add_url(self, url):
        # skip if 'url' is empty
        try:
            url
        except:
            return

        # check if url is not already in the "toCrawl" list
        if url not in self.to_crawl:
            # print "Add url: [%s]" % url
            self.to_crawl.append(url)

    '''
    extracting all keywords from the currently loaded page
    '''
    def extract_keywords(self):
        print "start extracting keywords"

        # if there is an empty page, or no page, then return an empty list
        try:
            self.current_page
        except:
            return []

        keywords = []

        # TODO
        # get all plain-text from website
        soup = bs(self.current_page)
        text = soup.findAll('p', text=True)
        # print text

        for word in text:
            # whitespace entfernen
            word.strip()

            if len(word) <= 3:
                continue

            singlewords = word.split()
            for w in singlewords:

                if len(w) <= 3:
                    continue

                print w

        # TODO
        # split plaintext into words

        # TODO
        # dump all words who's length <= 3

        # TODO (later)
        # remove all special characters like ,;-()_?!.[]{}\|/<>*%$#=+-"'`

        # TODO
        # return remaining keywords
        pass